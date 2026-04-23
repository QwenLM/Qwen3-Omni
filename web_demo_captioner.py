import os
import torch
from argparse import ArgumentParser

import gradio as gr
from qwen_omni_utils import process_mm_info
from transformers import Qwen3OmniMoeProcessor

os.environ['VLLM_USE_V1'] = '0'
os.environ['VLLM_WORKER_MULTIPROC_METHOD'] = 'spawn'

def _load_model_processor(args):
    if args.use_transformers:
        from transformers import Qwen3OmniMoeForConditionalGeneration
        if args.flash_attn2:
            model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
                args.checkpoint_path,
                dtype='auto',
                attn_implementation='flash_attention_2',
                device_map="auto"
            )
        else:
            model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
                args.checkpoint_path,
                device_map="auto",
                dtype='auto'
            )
    else:
        from vllm import LLM
        model = LLM(
            model=args.checkpoint_path,
            trust_remote_code=True,
            gpu_memory_utilization=0.95,
            tensor_parallel_size=torch.cuda.device_count(),
            limit_mm_per_prompt={'audio': 1},
            max_num_seqs=1,
            max_model_len=65536,
            seed=1234,
        )

    processor = Qwen3OmniMoeProcessor.from_pretrained(args.checkpoint_path)
    return model, processor


def _launch_demo(args, model, processor):
    use_transformers = args.use_transformers
    if not use_transformers:
        from vllm import SamplingParams

    def generate_caption_from_audio(audio_path, temperature, top_p, top_k):
        messages = [{
            "role": "user",
            "content": [
                {"type": "audio", "audio": audio_path},
            ],
        }]

        if use_transformers:
            text = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
            # use a prefix, such as a Chinese prompt, to support Chinese output
            # text = processor. apply_chat_template(messages, add_generation_prompt=False, tokenize=False)
            # text = text + "<|im_start|>assistant\n这个音频剪辑"

            audios, _, _ = process_mm_info(messages, use_audio_in_video=True)

            inputs = processor(text=text, audio=audios, return_tensors="pt", padding=True)
            inputs = inputs.to(model.device).to(model.dtype)

            output_ids = model.generate(
                **inputs,
                thinker_return_dict_in_generate=True,
                thinker_max_new_tokens=32768,
                thinker_do_sample=True,
                thinker_temperature=temperature,
                thinker_top_p=top_p,
                thinker_top_k=top_k,
                use_audio_in_video=True
            )

            response = processor.batch_decode(
                output_ids[:, inputs["input_ids"].shape[1]:],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=False,
            )[0]
            
            return response

        else:
            sampling_params = SamplingParams(
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                max_tokens=32768,
            )
            text = processor.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )
            audios, _, _ = process_mm_info(messages, use_audio_in_video=True)
            inputs = {
                'prompt': text,
                'multi_modal_data': {'audio': audios},
                "mm_processor_kwargs": {
                    "use_audio_in_video": True,
                },
            }
            outputs = model.generate(inputs, sampling_params=sampling_params)
            response = outputs[0].outputs[0].text
            return response

    def on_submit(audio_path, temperature, top_p, top_k):
        if not audio_path:
            yield None, gr.update(interactive=True)
            return

        caption = generate_caption_from_audio(audio_path, temperature, top_p, top_k)

        yield caption, gr.update(interactive=True)

    with gr.Blocks(theme=gr.themes.Soft(font=[gr.themes.GoogleFont("Source Sans Pro"), "Arial", "sans-serif"])) as demo:
        gr.Markdown("# Qwen3-Omni-30B-A3B-Captioner Demo")
        
        with gr.Row():
            with gr.Column(scale=1):
                audio_input = gr.Audio(sources=['upload', 'microphone'], type="filepath", label="Upload or record an audio")
                
                with gr.Accordion("Generation Parameters", open=True):
                    temperature = gr.Slider(label="Temperature", minimum=0.1, maximum=2.0, value=0.6, step=0.1)
                    top_p = gr.Slider(label="Top P", minimum=0.05, maximum=1.0, value=0.95, step=0.05)
                    top_k = gr.Slider(label="Top K", minimum=1, maximum=100, value=20, step=1)
                
                with gr.Row():
                    submit_btn = gr.Button("Submit", variant="primary")
                    clear_btn = gr.Button("Clear")

            with gr.Column(scale=2):
                output_caption = gr.Textbox(
                    label="Caption Result",
                    lines=15,
                    interactive=False
                )

        def clear_fields():
            return None, ""

        submit_btn.click(
            fn=on_submit,
            inputs=[audio_input, temperature, top_p, top_k],
            outputs=[output_caption, submit_btn]
        )

        clear_btn.click(fn=clear_fields, inputs=None, outputs=[audio_input, output_caption])
    
    demo.queue(default_concurrency_limit=1 if use_transformers else 100, max_size=100).launch(max_threads=100,
                                                                                            ssr_mode=False,
                                                                                            share=args.share,
                                                                                            inbrowser=args.inbrowser,
                                                                                            server_port=args.server_port,
                                                                                            server_name=args.server_name,)


DEFAULT_CKPT_PATH = "Qwen/Qwen3-Omni-30B-A3B-Captioner"

def _get_args():
    parser = ArgumentParser()

    parser.add_argument('-c', '--checkpoint-path', type=str, default=DEFAULT_CKPT_PATH,
                        help='Checkpoint name or path, default to %(default)r')
    parser.add_argument('--flash-attn2', action='store_true', default=False,
                        help='Enable flash_attention_2 when loading the model.')
    parser.add_argument('--use-transformers', action='store_true', default=False,
                        help='Use transformers for inference instead of vLLM.')
    parser.add_argument('--share', action='store_true', default=False,
                        help='Create a publicly shareable link for the interface.')
    parser.add_argument('--inbrowser', action='store_true', default=False,
                        help='Automatically launch the interface in a new tab on the default browser.')
    parser.add_argument('--server-port', type=int, default=8901, help='Demo server port.')
    parser.add_argument('--server-name', type=str, default='127.0.0.1', help='Demo server name.')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = _get_args()
    model, processor = _load_model_processor(args)
    _launch_demo(args, model, processor)
