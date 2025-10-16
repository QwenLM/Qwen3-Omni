# Qwen3-Omni

<br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com//Qwen3-Omni/qwen3_omni_logo.png" width="400"/>
<p>

<p align="center">
        💜 <a href="https://chat.qwen.ai/"><b>Qwen Chat</b></a>&nbsp&nbsp | &nbsp&nbsp🤗 <a href="https://huggingface.co/collections/Qwen/qwen3-omni-68d100a86cd0906843ceccbe">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/collections/Qwen3-Omni-867aef131e7d4f">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://qwen.ai/blog?id=65f766fc2dcba7905c1cb69cc4cab90e94126bf4&from=research.latest-advancements-list">Blog</a>&nbsp&nbsp | &nbsp&nbsp📚 <a href="https://github.com/QwenLM/Qwen3-Omni/tree/main/cookbooks">Cookbooks</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://arxiv.org/pdf/2509.17765">Paper</a>&nbsp&nbsp
<br>
🖥️ <a href="https://huggingface.co/spaces/Qwen/Qwen3-Omni-Demo">Hugging Face Demo</a>&nbsp&nbsp | &nbsp&nbsp 🖥️ <a href="https://modelscope.cn/studios/Qwen/Qwen3-Omni-Demo">ModelScope Demo</a>&nbsp&nbsp | &nbsp&nbsp💬 <a href="https://github.com/QwenLM/Qwen/blob/main/assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp🫨 <a href="https://discord.gg/CV4E9rpNSD">Discord</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://help.aliyun.com/zh/model-studio/user-guide/qwen-omni">API</a>

</p>

We release **Qwen3-Omni**, the natively end-to-end multilingual omni-modal foundation models. It is designed to process diverse inputs including text, images, audio, and video, while delivering real-time streaming responses in both text and natural speech. Click the video below for more information 😃

<details open>
<summary>English Version</summary>
<a href="https://youtu.be/_zdOrPju4_g" target="_blank">
  <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/videocover.png" alt="Open English Video"/>
</a>
</details>

<details>
<summary>Chinese Version</summary>
<a href="https://youtu.be/Wtjsw5deXfQ" target="_blank">
  <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/videocover.png" alt="打开中文视频"/>
</a>
</details>


## News
* 2025.09.26: ⭐️⭐️⭐️ Qwen3-Omni reaches top-1 on Hugging Face Trending! 
* 2025.09.22: 🎉🎉🎉 We have released [Qwen3-Omni](https://huggingface.co/collections/Qwen/qwen3-omni-68d100a86cd0906843ceccbe). For more details, please check our [blog](https://qwen.ai/blog?id=65f766fc2dcba7905c1cb69cc4cab90e94126bf4&from=research.latest-advancements-list)!

## Contents <!-- omit in toc -->

- [Overview](#overview)
  - [Introduction](#introduction)
  - [Model Architecture](#model-architecture)
  - [Cookbooks for Usage Cases](#cookbooks-for-usage-cases)
- [QuickStart](#quickstart)
  - [Model Description and Download](#model-description-and-download)
  - [Transformers Usage](#transformers-usage)
  - [vLLM Usage](#vllm-usage)
  - [DashScope API Usage](#dashscope-api-usage)
  - [Usage Tips (Recommended Reading)](#usage-tips-recommended-reading)
- [Interaction with Qwen3-Omni](#interaction-with-qwen3-omni)
  - [Online Demo](#online-demo)
  - [Real-Time Interaction](#real-time-interaction)
  - [Launch Local Web UI Demo](#launch-local-web-ui-demo)
- [Docker](#-docker)
- [Evaluation](#evaluation)
  - [Performance of Qwen3-Omni](#performance-of-qwen3-omni)
  - [Setting for Evaluation](#setting-for-evaluation)
- [Citation](#citation)

## Overview
### Introduction

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/q3o_introduction.png" width="90%"/>
<p>

Qwen3-Omni is the natively end-to-end multilingual omni-modal foundation models. It processes text, images, audio, and video, and delivers real-time streaming responses in both text and natural speech. We introduce several architectural upgrades to improve performance and efficiency. Key features:

* **State-of-the-art across modalities**: Early text-first pretraining and mixed multimodal training provide native multimodal support. While achieving strong audio and audio-video results, unimodal text and image performance does not regress. Reaches SOTA on 22 of 36 audio/video benchmarks and open-source SOTA on 32 of 36; ASR, audio understanding, and voice conversation performance is comparable to Gemini 2.5 Pro.

* **Multilingual**: Supports 119 text languages, 19 speech input languages, and 10 speech output languages.
  - **Speech Input**: English, Chinese, Korean, Japanese, German, Russian, Italian, French, Spanish, Portuguese, Malay, Dutch, Indonesian, Turkish, Vietnamese, Cantonese, Arabic, Urdu.
  - **Speech Output**: English, Chinese, French, German, Russian, Italian, Spanish, Portuguese, Japanese, Korean.

* **Novel Architecture**: MoE-based Thinker–Talker design with AuT pretraining for strong general representations, plus a multi-codebook design that drives latency to a minimum.

* **Real-time Audio/Video Interaction**: Low-latency streaming with natural turn-taking and immediate text or speech responses.

* **Flexible Control**: Customize behavior via system prompts for fine-grained control and easy adaptation.

* **Detailed Audio Captioner**: Qwen3-Omni-30B-A3B-Captioner is now open source: a general-purpose, highly detailed, low-hallucination audio captioning model that fills a critical gap in the open-source community.

### Model Architecture

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/overview.png" width="80%"/>
<p>

### Cookbooks for Usage Cases

Qwen3-Omni supports a wide range of multimodal application scenarios, covering various domain tasks involving audio, image, video, and audio-visual modalities. Below are several cookbooks demonstrating the usage cases of Qwen3-Omni and these cookbooks include our actual execution logs. You can first follow the [QuickStart](#quickstart) guide to download the model and install the necessary inference environment dependencies, then run and experiment locally—try modifying prompts or switching model types, and enjoy exploring the capabilities of Qwen3-Omni!

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Cookbook</th>
      <th>Description</th>
      <th>Open</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">Audio</td>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/speech_recognition.ipynb">Speech Recognition</a></td>
      <td>Speech recognition, supporting multiple languages and long audio.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/speech_recognition.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/speech_translation.ipynb">Speech Translation</a></td>
      <td>Speech-to-Text / Speech-to-Speech translation.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/speech_translation.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/music_analysis.ipynb">Music Analysis</a></td>
      <td>Detailed analysis and appreciation of any music, including style, genre, rhythm, etc.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/music_analysis.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/sound_analysis.ipynb">Sound Analysis</a></td>
      <td>Description and analysis of various sound effects and audio signals.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/sound_analysis.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_caption.ipynb">Audio Caption</a></td>
      <td>Audio captioning, detailed description of any audio input.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_caption.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/mixed_audio_analysis.ipynb">Mixed Audio Analysis</a></td>
      <td>Analysis of mixed audio content, such as speech, music, and environmental sounds.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/mixed_audio_analysis.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td rowspan="7">Visual</td>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/ocr.ipynb">OCR</a></td>
      <td>OCR for complex images.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/ocr.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/object_grounding.ipynb">Object Grounding</a></td>
      <td>Target detection and grounding.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/object_grounding.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/image_question.ipynb">Image Question</a></td>
      <td>Answering arbitrary questions about any image.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/image_question.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/image_math.ipynb">Image Math</a></td>
      <td>Solving complex mathematical problems in images, highlighting the capabilities of the Thinking model.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/image_math.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/video_description.ipynb">Video Description</a></td>
      <td>Detailed description of video content.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/video_description.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/video_navigation.ipynb">Video Navigation</a></td>
      <td>Generating navigation commands from first-person motion videos.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/video_navigation.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/video_scene_transition.ipynb">Video Scene Transition</a></td>
      <td>Analysis of scene transitions in videos.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/video_scene_transition.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td rowspan="3">Audio-Visual</td>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_visual_question.ipynb">Audio Visual Question</a></td>
      <td>Answering arbitrary questions in audio-visual scenarios, demonstrating the model's ability to model temporal alignment between audio and video.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_visual_question.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_visual_interaction.ipynb">Audio Visual Interaction</a></td>
      <td>Interactive communication with the model using audio-visual inputs, including task specification via audio.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_visual_interaction.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_visual_dialogue.ipynb">Audio Visual Dialogue</a></td>
      <td>Conversational interaction with the model using audio-visual inputs, showcasing its capabilities in casual chat and assistant-like behavior.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_visual_dialogue.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td>Agent</td>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_function_call.ipynb">Audio Function Call</a></td>
      <td>Using audio input to perform function calls, enabling agent-like behaviors.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/audio_function_call.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
    <tr>
      <td>Downstream Task Fine-tuning</td>
      <td><a href="https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/omni_captioner.ipynb">Omni Captioner</a></td>
      <td>Introduction and capability demonstration of <strong>Qwen3-Omni-30B-A3B-Captioner</strong>, a downstream fine-tuned model based on Qwen3-Omni-30B-A3B-Instruct, illustrating the strong generalization ability of the Qwen3-Omni foundation model.</td>
      <td><a href="https://colab.research.google.com/github/QwenLM/Qwen3-Omni/blob/main/cookbooks/omni_captioner.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
    </tr>
  </tbody>
</table>

## QuickStart

Here, we provide several methods to quickly get started with Qwen3-Omni. If you want complete experience of Qwen3-Omni, you can use [Hugging Face Transformers](#transformers-usage). However, since Qwen3-Omni employs an MoE architecture, inference speed with Hugging Face Transformers on MoE models can be very slow. For large-scale invocation or low-latency requirements, we highly recommend using [vLLM](#vllm-usage) or performing inference via the [DashScope API](#dashscope-api-usage). We also strongly suggest using our provided [Docker](#-docker) image, which includes a complete runtime environment for both Hugging Face Transformers and vLLM. In addition, our [cookbooks](https://github.com/QwenLM/Qwen3-Omni/tree/main/cookbooks) offer some use cases to show Qwen3-Omni's capabilities. Welcome to learn more!

### Model Description and Download

Below is the description of all Qwen3-Omni models. Please select and download the model that fits your needs.

| Model Name                   | Description |
|------------------------------|-------------|
| Qwen3-Omni-30B-A3B-Instruct  | The Instruct model of Qwen3-Omni-30B-A3B, containing both thinker and talker, supporting audio, video, and text input, with audio and text output. For more information, please read the [Qwen3-Omni Technical Report](https://arxiv.org/pdf/2509.17765). |
| Qwen3-Omni-30B-A3B-Thinking  | The Thinking model of Qwen3-Omni-30B-A3B, containing the thinker component, equipped with chain-of-thought reasoning, supporting audio, video, and text input, with text output. For more information, please read the [Qwen3-Omni Technical Report](https://arxiv.org/pdf/2509.17765).|
| Qwen3-Omni-30B-A3B-Captioner | A downstream audio fine-grained caption model fine-tuned from Qwen3-Omni-30B-A3B-Instruct, which produces detailed, low-hallucination captions for arbitrary audio inputs. It contains the thinker, supporting audio input and text output. For more information, you can refer to the model's [cookbook](https://github.com/QwenLM/Qwen3-Omni/blob/main/cookbooks/omni_captioner.ipynb) or [Hugging Face Demo](https://huggingface.co/spaces/Qwen/Qwen3-Omni-Captioner-Demo) and [ModelScope Demo](https://modelscope.cn/studios/Qwen/Qwen3-Omni-Captioner-Demo). |

During loading in Hugging Face Transformers or vLLM, model weights will be automatically downloaded based on the model name. However, if your runtime environment is not conducive to downloading weights during execution, you can refer to the following commands to manually download the model weights to a local directory:

```bash
# Download through ModelScope (recommended for users in Mainland China)
pip install -U modelscope
modelscope download --model Qwen/Qwen3-Omni-30B-A3B-Instruct --local_dir ./Qwen3-Omni-30B-A3B-Instruct
modelscope download --model Qwen/Qwen3-Omni-30B-A3B-Thinking --local_dir ./Qwen3-Omni-30B-A3B-Thinking
modelscope download --model Qwen/Qwen3-Omni-30B-A3B-Captioner --local_dir ./Qwen3-Omni-30B-A3B-Captioner

# Download through Hugging Face
pip install -U "huggingface_hub[cli]"
huggingface-cli download Qwen/Qwen3-Omni-30B-A3B-Instruct --local-dir ./Qwen3-Omni-30B-A3B-Instruct
huggingface-cli download Qwen/Qwen3-Omni-30B-A3B-Thinking --local-dir ./Qwen3-Omni-30B-A3B-Thinking
huggingface-cli download Qwen/Qwen3-Omni-30B-A3B-Captioner --local-dir ./Qwen3-Omni-30B-A3B-Captioner
```

### Transformers Usage

#### Installation

The Hugging Face Transformers code for Qwen3-Omni has been successfully merged, but the PyPI package has not yet been released. Therefore, you need to install it from source using the following command. We strongly recommend that you **create a new Python environment** or use our [Docker](#-docker) to avoid environment runtime issues.

```bash
# If you already have transformers installed, please uninstall it first, or create a new Python environment
# pip uninstall transformers
pip install transformers==4.57
pip install accelerate
```

We offer a toolkit to help you handle various types of audio and visual input more conveniently, providing an API-like experience. This includes support for base64, URLs, and interleaved audio, images, and videos. You can install it using the following command and make sure your system has `ffmpeg` installed:

```bash
pip install qwen-omni-utils -U
```

Additionally, we recommend using FlashAttention 2 when running with Hugging Face Transformers to reduce GPU memory usage. However, if you are primarily using [vLLM](#vllm-usage) for inference, this installation is not necessary, as vLLM includes FlashAttention 2 by default.

```bash
pip install -U flash-attn --no-build-isolation
```

Also, you should have hardware that is compatible with FlashAttention 2. Read more about it in the official documentation of the [FlashAttention repository](https://github.com/Dao-AILab/flash-attention). FlashAttention 2 can only be used when a model is loaded in `torch.float16` or `torch.bfloat16`.

#### Code Snippet

Here is a code snippet to show you how to use Qwen3-Omni with `transformers` and `qwen_omni_utils`:

```python
import soundfile as sf

from transformers import Qwen3OmniMoeForConditionalGeneration, Qwen3OmniMoeProcessor
from qwen_omni_utils import process_mm_info

MODEL_PATH = "Qwen/Qwen3-Omni-30B-A3B-Instruct"
# MODEL_PATH = "Qwen/Qwen3-Omni-30B-A3B-Thinking"

model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
    MODEL_PATH,
    dtype="auto",
    device_map="auto",
    attn_implementation="flash_attention_2",
)

processor = Qwen3OmniMoeProcessor.from_pretrained(MODEL_PATH)

conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg"},
            {"type": "audio", "audio": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cough.wav"},
            {"type": "text", "text": "What can you see and hear? Answer in one short sentence."}
        ],
    },
]

# Set whether to use audio in video
USE_AUDIO_IN_VIDEO = True

# Preparation for inference
text = processor.apply_chat_template(conversation, add_generation_prompt=True, tokenize=False)
audios, images, videos = process_mm_info(conversation, use_audio_in_video=USE_AUDIO_IN_VIDEO)
inputs = processor(text=text, 
                   audio=audios, 
                   images=images, 
                   videos=videos, 
                   return_tensors="pt", 
                   padding=True, 
                   use_audio_in_video=USE_AUDIO_IN_VIDEO)
inputs = inputs.to(model.device).to(model.dtype)

# Inference: Generation of the output text and audio
text_ids, audio = model.generate(**inputs, 
                                 speaker="Ethan", 
                                 thinker_return_dict_in_generate=True,
                                 use_audio_in_video=USE_AUDIO_IN_VIDEO)

text = processor.batch_decode(text_ids.sequences[:, inputs["input_ids"].shape[1] :],
                              skip_special_tokens=True,
                              clean_up_tokenization_spaces=False)
print(text)
if audio is not None:
    sf.write(
        "output.wav",
        audio.reshape(-1).detach().cpu().numpy(),
        samplerate=24000,
    )
```

Here are some more advanced usage examples. You can expand the sections below to learn more.

<details>
<summary>Batch inference</summary>

The model can batch inputs composed of mixed samples of various types such as text, images, audio, and videos as input when `return_audio=False` is set. Here is an example.

```python
from transformers import Qwen3OmniMoeForConditionalGeneration, Qwen3OmniMoeProcessor
from qwen_omni_utils import process_mm_info

MODEL_PATH = "Qwen/Qwen3-Omni-30B-A3B-Instruct"
# MODEL_PATH = "Qwen/Qwen3-Omni-30B-A3B-Thinking"

model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
    MODEL_PATH,
    dtype="auto",
    device_map="auto",
    attn_implementation="flash_attention_2",
)
model.disable_talker()

processor = Qwen3OmniMoeProcessor.from_pretrained(MODEL_PATH)

# Conversation with image only
conversation1 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg"},
            {"type": "text", "text": "What can you see in this image? Answer in one sentence."},
        ]
    }
]

# Conversation with audio only
conversation2 = [
    {
        "role": "user",
        "content": [
            {"type": "audio", "audio": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cough.wav"},
            {"type": "text", "text": "What can you hear in this audio?"},
        ]
    }
]

# Conversation with pure text and system prompt
conversation3 = [
    {
        "role": "system",
        "content": [
            {"type": "text", "text": "You are Qwen-Omni."}
        ],
    },
    {
        "role": "user",
        "content": "Who are you?"
    }
]

# Conversation with mixed media
conversation4 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg"},
            {"type": "audio", "audio": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cough.wav"},
            {"type": "text", "text": "What can you see and hear? Answer in one sentence."}
        ],
    }
]

# Combine messages for batch processing
conversations = [conversation1, conversation2, conversation3, conversation4]

# Set whether to use audio in video
USE_AUDIO_IN_VIDEO = True

# Preparation for batch inference
text = processor.apply_chat_template(conversations, add_generation_prompt=True, tokenize=False)
audios, images, videos = process_mm_info(conversations, use_audio_in_video=USE_AUDIO_IN_VIDEO)

inputs = processor(text=text, 
                   audio=audios, 
                   images=images, 
                   videos=videos, 
                   return_tensors="pt", 
                   padding=True, 
                   use_audio_in_video=USE_AUDIO_IN_VIDEO)
inputs = inputs.to(model.device).to(model.dtype)

# Batch inference does not support returning audio
text_ids, audio = model.generate(**inputs,
                                 return_audio=False,
                                 thinker_return_dict_in_generate=True,
                                 use_audio_in_video=USE_AUDIO_IN_VIDEO)

text = processor.batch_decode(text_ids.sequences[:, inputs["input_ids"].shape[1] :],
                              skip_special_tokens=True,
                              clean_up_tokenization_spaces=False)
print(text)
```

</details>

<details>
<summary>Use audio output or not</summary>

The model supports both text and audio outputs. If users do not need audio outputs, they can call `model.disable_talker()` after initializing the model. This option will save about `10GB` of GPU memory, but the `return_audio` option for the `generate` function will only allow `False`.
```python
model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-Omni-30B-A3B-Instruct",
    dtype="auto",
    device_map="auto",
    attn_implementation="flash_attention_2",
)
model.disable_talker()
```

For a more flexible experience, we recommend that users decide whether to return audio when the `generate` function is called. If `return_audio` is set to `False`, the model will only return text outputs, resulting in faster text responses.

```python
model = Qwen3OmniMoeForConditionalGeneration.from_pretrained(
    "Qwen/Qwen3-Omni-30B-A3B-Instruct",
    dtype="auto",
    device_map="auto",
    attn_implementation="flash_attention_2",
)
...
text_ids, _ = model.generate(..., return_audio=False)```

</details>

<details>
<summary>Change voice type of output audio</summary>

Qwen3-Omni supports changing the voice of the output audio. The `"Qwen/Qwen3-Omni-30B-A3B-Instruct"` checkpoint supports three voice types as follows:

| Voice Type | Gender | Description |
|------------|--------|-------------|
| Ethan      | Male   | A bright, upbeat voice with infectious energy and a warm, approachable vibe. |
| Chelsie    | Female | A honeyed, velvety voice that carries a gentle warmth and luminous clarity. |
| Aiden      | Male   | A warm, laid-back American voice with a gentle, boyish charm. |

Users can use the `speaker` parameter of the `generate` function to specify the voice type. By default, if `speaker` is not specified, the voice type is `Ethan`.

```python
text_ids, audio = model.generate(..., speaker="Ethan")
```

```python
text_ids, audio = model.generate(..., speaker="Chelsie")
```

```python
text_ids, audio = model.generate(..., speaker="Aiden")
```

</details>

Additionally, for more usage details such as prompt settings, task-specific usage methods, and resource requirements, please refer to [Usage Tips](#usage-tips-recommended-reading) and [Cookbooks for Usage Cases](#cookbooks-for-usage-cases).

### vLLM Usage

#### Installation

We strongly recommend using vLLM for inference and deployment of the Qwen3-Omni series models. Since our code is currently in the pull request stage, and **audio output inference support for the Instruct model will be released in the near future**, you can follow the commands below to install vLLM from source. Please note that we recommend you **create a new Python environment** or use our provided [Docker](#-docker) to avoid runtime environment conflicts and incompatibilities. For more details on compiling vLLM from source, please refer to the [vLLM official documentation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#set-up-using-python-only-build-without-compilation).

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
python3 -m venv venv
source .venv/bin/activate
VLLM_USE_PRECOMPILED=1 pip install -e .
# If you want to build from scratch on a specific commit, then skip VLLM_USE_PRECOMPILED and just do:
#   pip install -e .
pip install qwen-omni-utils -U
pip install vllm[audio]
```

#### Inference

You can use the following code for vLLM inference. The `limit_mm_per_prompt` parameter specifies the maximum number of each modality's data allowed per message. Since vLLM needs to pre-allocate GPU memory, larger values will require more GPU memory; if OOM issues occur, try reducing this value. Setting `tensor_parallel_size` greater than one enables multi-GPU parallel inference, improving concurrency and throughput. In addition, `max_num_seqs` indicates the number of sequences that vLLM processes in parallel during each inference step. A larger value requires more GPU memory but enables higher batch inference speed. For more details, please refer to the [vLLM official documentation](https://docs.vllm.ai/en/latest/api/vllm/index.html#vllm.LLM). Below is a simple example of how to run Qwen3-Omni with vLLM:

```python
import os
import torch

from vllm import LLM, SamplingParams
from transformers import Qwen3OmniMoeProcessor
from qwen_omni_utils import process_mm_info

if __name__ == '__main__':
    # vLLM engine v1 not supported yet
    os.environ['VLLM_USE_V1'] = '0'

    MODEL_PATH = "Qwen/Qwen3-Omni-30B-A3B-Instruct"
    # MODEL_PATH = "Qwen/Qwen3-Omni-30B-A3B-Thinking"

    llm = LLM(
            model=MODEL_PATH, trust_remote_code=True, gpu_memory_utilization=0.95,
            tensor_parallel_size=torch.cuda.device_count(),
            limit_mm_per_prompt={'image': 3, 'video': 3, 'audio': 3},
            max_num_seqs=8,
            max_model_len=32768,
            seed=1234,
    )

    sampling_params = SamplingParams(
        temperature=0.6,
        top_p=0.95,
        top_k=20,
        max_tokens=16384,
    )

    processor = Qwen3OmniMoeProcessor.from_pretrained(MODEL_PATH)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "video", "video": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/draw.mp4"}
            ], 
        }
    ]

    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    audios, images, videos = process_mm_info(messages, use_audio_in_video=True)

    inputs = {
        'prompt': text,
        'multi_modal_data': {},
        "mm_processor_kwargs": {
            "use_audio_in_video": True,
        },
    }

    if images is not None:
        inputs['multi_modal_data']['image'] = images
    if videos is not None:
        inputs['multi_modal_data']['video'] = videos
    if audios is not None:
        inputs['multi_modal_data']['audio'] = audios

    outputs = llm.generate([inputs], sampling_params=sampling_params)

    print(outputs[0].outputs[0].text)
```

Here are some more advanced usage examples. You can expand the sections below to learn more.

<details>
<summary>Batch inference</summary>

Using vLLM enables fast batch inference, which can help you efficiently process large volumes of data or conduct benchmarking. Refer to the following code example:

```python
import os
import torch

from vllm import LLM, SamplingParams
from transformers import Qwen3OmniMoeProcessor
from qwen_omni_utils import process_mm_info

def build_input(processor, messages, use_audio_in_video):
    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    audios, images, videos = process_mm_info(messages, use_audio_in_video=use_audio_in_video)

    inputs = {
        'prompt': text,
        'multi_modal_data': {},
        "mm_processor_kwargs": {
            "use_audio_in_video": use_audio_in_video,
        },
    }

    if images is not None:
        inputs['multi_modal_data']['image'] = images
    if videos is not None:
        inputs['multi_modal_data']['video'] = videos
    if audios is not None:
        inputs['multi_modal_data']['audio'] = audios
    
    return inputs

if __name__ == '__main__':
    # vLLM engine v1 not supported yet
    os.environ['VLLM_USE_V1'] = '0'

    MODEL_PATH = "Qwen/Qwen3-Omni-30B-A3B-Instruct"
    # MODEL_PATH = "Qwen/Qwen3-Omni-30B-A3B-Thinking"

    llm = LLM(
            model=MODEL_PATH, trust_remote_code=True, gpu_memory_utilization=0.95,
            tensor_parallel_size=torch.cuda.device_count(),
            limit_mm_per_prompt={'image': 3, 'video': 3, 'audio': 3},
            max_num_seqs=8,
            max_model_len=32768,
            seed=1234,
    )

    sampling_params = SamplingParams(
        temperature=0.6,
        top_p=0.95,
        top_k=20,
        max_tokens=16384,
    )

    processor = Qwen3OmniMoeProcessor.from_pretrained(MODEL_PATH)

    # Conversation with image only
    conversation1 = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg"},
                {"type": "text", "text": "What can you see in this image? Answer in one sentence."},
            ]
        }
    ]

    # Conversation with audio only
    conversation2 = [
        {
            "role": "user",
            "content": [
                {"type": "audio", "audio": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cough.wav"},
                {"type": "text", "text": "What can you hear in this audio?"},
            ]
        }
    ]

    # Conversation with pure text and system prompt
    conversation3 = [
        {
            "role": "system",
            "content": [
                {"type": "text", "text": "You are Qwen-Omni."}
            ],
        },
        {
            "role": "user",
            "content": "Who are you? Answer in one sentence."
        }
    ]

    # Conversation with mixed media
    conversation4 = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg"},
                {"type": "audio", "audio": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/cookbook/asr_fr.wav"},
                {"type": "text", "text": "What can you see and hear? Answer in one sentence."}
            ],
        }
    ]
    
    USE_AUDIO_IN_VIDEO = True

    # Combine messages for batch processing
    conversations = [conversation1, conversation2, conversation3, conversation4]
    inputs = [build_input(processor, messages, USE_AUDIO_IN_VIDEO) for messages in conversations]

    outputs = llm.generate(inputs, sampling_params=sampling_params)

    result = [outputs[i].outputs[0].text for i in range(len(outputs))]
    print(result)
```

</details>

<details>
<summary>vLLM Serve Usage</summary>

vLLM serve for Qwen3-Omni currently only supports the thinker model. The `use_audio_in_video` parameter is not available in vLLM serve; you can handle this by separately passing video and audio inputs for processing. You can start vLLM serve through the following command:

```bash
# Qwen3-Omni-30B-A3B-Instruct for single GPU
vllm serve Qwen/Qwen3-Omni-30B-A3B-Instruct --port 8901 --host 127.0.0.1 --dtype bfloat16 --max-model-len 32768 --allowed-local-media-path / -tp 1
# Qwen3-Omni-30B-A3B-Instruct for multi-GPU (example on 4 GPUs)
vllm serve Qwen/Qwen3-Omni-30B-A3B-Instruct --port 8901 --host 127.0.0.1 --dtype bfloat16 --max-model-len 65536 --allowed-local-media-path / -tp 4
# Qwen/Qwen3-Omni-30B-A3B-Thinking for single GPU
vllm serve Qwen/Qwen3-Omni-30B-A3B-Thinking --port 8901 --host 127.0.0.1 --dtype bfloat16 --max-model-len 32768 --allowed-local-media-path / -tp 1
# Qwen/Qwen3-Omni-30B-A3B-Thinking for multi-GPU (example on 4 GPUs)
vllm serve Qwen/Qwen3-Omni-30B-A3B-Thinking --port 8901 --host 127.0.0.1 --dtype bfloat16 --max-model-len 65536 --allowed-local-media-path / -tp 4
```

Then you can use the chat API as below (via curl, for example):
```bash
curl http://localhost:8901/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg"}},
        {"type": "audio_url", "audio_url": {"url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cough.wav"}},
        {"type": "text", "text": "What can you see and hear? Answer in one sentence."}
    ]}
    ]
    }'
```

</details>

Additionally, for more usage details such as prompt settings, task-specific usage methods, and resource requirements, please refer to [Usage Tips](#usage-tips-recommended-reading) and [Cookbooks for Usage Cases](#cookbooks-for-usage-cases).

### DashScope API Usage

To further explore Qwen3-Omni, we encourage you to try our DashScope API for a faster and more efficient experience. For detailed API information and documentation, please refer to the following:

| API Description | API Documentation (Mainland China) | API Documentation (International) |
|------------------|-----------------------------------|------------------------------------|
| Offline API for Qwen3-Omni-Flash, including Instruct and Thinking models | [https://help.aliyun.com/zh/model-studio/qwen-omni](https://help.aliyun.com/zh/model-studio/qwen-omni) | [https://www.alibabacloud.com/help/en/model-studio/qwen-omni](https://www.alibabacloud.com/help/en/model-studio/qwen-omni) |
| Real-time API for Qwen3-Omni-Flash, supporting end-to-end real-time interaction | [https://help.aliyun.com/zh/model-studio/realtime](https://help.aliyun.com/zh/model-studio/realtime) | [https://www.alibabacloud.com/help/en/model-studio/realtime](https://www.alibabacloud.com/help/en/model-studio/realtime) |
| API for Qwen3-Omni-30B-A3B-Captioner model | [https://help.aliyun.com/zh/model-studio/qwen3-omni-captioner](https://help.aliyun.com/zh/model-studio/qwen3-omni-captioner) | [https://www.alibabacloud.com/help/zh/model-studio/qwen3-omni-captioner](https://www.alibabacloud.com/help/zh/model-studio/qwen3-omni-captioner) |

### Usage Tips (Recommended Reading)

#### Minimum GPU memory requirements

| Model                        | Precision | 15s Video | 30s Video | 60s Video | 120s Video   |
|------------------------------|-----------| --------- | --------- | --------- | --------- |
| Qwen3-Omni-30B-A3B-Instruct  | BF16      | 78.85 GB  | 88.52 GB  | 107.74 GB | 144.81 GB |
| Qwen3-Omni-30B-A3B-Thinking  | BF16      | 68.74 GB  | 77.79 GB  | 95.76 GB  | 131.65 GB  |

**Note**: The table above presents the theoretical minimum memory requirements for inference with `transformers` and `BF16` precision, tested with `attn_implementation="flash_attention_2"`. The Instruct model includes both the **thinker** and **talker** components, whereas the Thinking model includes only the **thinker** part.

#### Prompt for Audio-Visual Interaction

When using Qwen3-Omni for audio-visual multimodal interaction, where the input consists of a video and its corresponding audio (with the audio serving as a query), we recommend using the **following system prompt**. This setup helps the model maintain high reasoning capability while better assuming interactive roles such as a smart assistant. Additionally, the text generated by the thinker will be more readable, with a natural, conversational tone and without complex formatting that is difficult to vocalize, leading to more stable and fluent audio output from the talker. You can customize the `user_system_prompt` field in the system prompt to include character settings or other role-specific descriptions as needed.

```
user_system_prompt = "You are Qwen-Omni, a smart voice assistant created by Alibaba Qwen."
message = {
    "role": "system",
    "content": [
          {"type": "text", "text": f"{user_system_prompt} You are a virtual voice assistant with no gender or age.\nYou are communicating with the user.\nIn user messages, “I/me/my/we/our” refer to the user and “you/your” refer to the assistant. In your replies, address the user as “you/your” and yourself as “I/me/my”; never mirror the user’s pronouns—always shift perspective. Keep original pronouns only in direct quotes; if a reference is unclear, ask a brief clarifying question.\nInteract with users using short(no more than 50 words), brief, straightforward language, maintaining a natural tone.\nNever use formal phrasing, mechanical expressions, bullet points, overly structured language. \nYour output must consist only of the spoken content you want the user to hear. \nDo not include any descriptions of actions, emotions, sounds, or voice changes. \nDo not use asterisks, brackets, parentheses, or any other symbols to indicate tone or actions. \nYou must answer users' audio or text questions, do not directly describe the video content. \nYou should communicate in the same language strictly as the user unless they request otherwise.\nWhen you are uncertain (e.g., you can't see/hear clearly, don't understand, or the user makes a comment rather than asking a question), use appropriate questions to guide the user to continue the conversation.\nKeep replies concise and conversational, as if talking face-to-face."}
    ]
}
```

#### Best Practices for the Thinking Model

The `Qwen3-Omni-30B-A3B-Thinking` model is primarily designed for understanding and interacting with multimodal inputs, including text, audio, image, and video. To achieve optimal performance, we recommend that users include an explicit textual instruction or task description in each round of dialogue alongside the multimodal input. This helps clarify the intent and significantly enhances the model's ability to leverage its reasoning capabilities. For example:

```python
messages = [
    {
        "role": "user",
        "content": [
            {"type": "audio", "audio": "/path/to/audio.wav"},
            {"type": "image", "image": "/path/to/image.png"},
            {"type": "video", "video": "/path/to/video.mp4"},
            {"type": "text", "text": "Analyze this audio, image, and video together."},
        ], 
    }
]
```

#### Use audio in video

In multimodal interaction, user-provided videos are often accompanied by audio (such as spoken questions or sounds from events in the video). This information helps the model provide a better interactive experience. We provide the following options for users to decide whether to use the audio from a video.

```python
# In data preprocessing
audios, images, videos = process_mm_info(messages, use_audio_in_video=True)
```

```python
# For Transformers
text = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
inputs = processor(text=text, audio=audios, images=images, videos=videos, return_tensors="pt", 
                   padding=True, use_audio_in_video=True)
text_ids, audio = model.generate(..., use_audio_in_video=True)

# For vLLM
text = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
inputs = {
    'prompt': text,
    'multi_modal_data': {},
    "mm_processor_kwargs": {
        "use_audio_in_video": True,
    },
}
```

It is worth noting that during a multi-round conversation, the `use_audio_in_video` parameter must be set consistently across these steps; otherwise, unexpected results may occur.

## Interaction with Qwen3-Omni

### Online Demo

Without local deployment, you can experience an online web demo directly by visiting our [Hugging Face Spaces](https://huggingface.co/spaces/Qwen/Qwen3-Omni-Demo) and [ModelScope Studio](https://modelscope.cn/studios/Qwen/Qwen3-Omni-Demo). This includes quick hands-on experiences for Qwen3-Omni-Realtime, Qwen3-Omni (Instruct and Thinking), and Qwen3-Omni-30B-A3B-Captioner.

### Real-Time Interaction

Real-time streaming interaction with Qwen3-Omni is available now. Please visit [Qwen Chat](https://chat.qwen.ai/) and select the voice/video call option in the chat box to experience it.

### Launch Local Web UI Demo

In this section, we provide instructions for users to build a web-based user interface (UI) demo. This UI demo allows users to interact with the model through a web browser. Follow the steps below to get start :)

#### Installation

Before you begin, we strongly recommend that you refer to the **Installation** section in [vLLM Usage](#vllm-usage) to set up your environment, which will allow you to seamlessly use both the vLLM and Transformers backends. However, if you only intend to use the Transformers backend (**note that this will result in significantly slower inference**), please follow the installation instructions in [Transformers Usage](#transformers-usage). That said, we still highly recommend using our [Docker](#-docker) image to avoid potential environment-related issues. Additionally, if you are running locally, make sure your system has `ffmpeg` installed and you install the following dependencies:

```bash
pip install gradio==5.44.1 gradio_client==1.12.1 soundfile==0.13.1
```

#### Running the Demo

Once the required packages are installed, you can launch the web demo using the following commands. These commands will start a web server and provide you with a link to access the UI in your web browser. You can run `python web_demo.py --help` and `python web_demo_captioner.py --help` to learn about more options.

```bash
# For Qwen3-Omni-30B-A3B-Instruct with vLLM backend
python web_demo.py -c Qwen/Qwen3-Omni-30B-A3B-Instruct
# For Qwen3-Omni-30B-A3B-Instruct with Transformers backend
python web_demo.py -c Qwen/Qwen3-Omni-30B-A3B-Instruct --use-transformers --generate-audio
# For Qwen3-Omni-30B-A3B-Instruct with Transformers backend and FlashAttention support
python web_demo.py -c Qwen/Qwen3-Omni-30B-A3B-Instruct --use-transformers --generate-audio --flash-attn2
```

```bash
# For Qwen3-Omni-30B-A3B-Thinking with vLLM backend
python web_demo.py -c Qwen/Qwen3-Omni-30B-A3B-Thinking
# For Qwen3-Omni-30B-A3B-Thinking with Transformers backend
python web_demo.py -c Qwen/Qwen3-Omni-30B-A3B-Thinking --use-transformers
# For Qwen3-Omni-30B-A3B-Thinking with Transformers backend and FlashAttention support
python web_demo.py -c Qwen/Qwen3-Omni-30B-A3B-Thinking --use-transformers --flash-attn2
```

```bash
# For Qwen3-Omni-30B-A3B-Captioner with vLLM backend
python web_demo_captioner.py -c Qwen/Qwen3-Omni-30B-A3B-Captioner
# For Qwen3-Omni-30B-A3B-Captioner with Transformers backend
python web_demo_captioner.py -c Qwen/Qwen3-Omni-30B-A3B-Captioner --use-transformers
# For Qwen3-Omni-30B-A3B-Captioner with Transformers backend and FlashAttention support
python web_demo_captioner.py -c Qwen/Qwen3-Omni-30B-A3B-Captioner --use-transformers --flash-attn2
```

After running the command, you’ll see a link generated in the terminal similar to this:

```
Running on local: http://127.0.0.1:8901/
```

If you are running locally, copy this link and paste it into your browser to access the web UI. If you are running on a server or in a `docker` container, please configure the address according to the server's actual IP, or set up port forwarding where necessary. For instructions on how to configure port forwarding from the official `docker` container to the host machine, please refer to [here](#-docker).

## 🐳 Docker

To simplify the deployment process, we provide Docker images with pre-built environments: [qwenllm/qwen3-omni](https://hub.docker.com/r/qwenllm/qwen3-omni). You only need to install the driver and download model files to launch the demos. Please refer to the [guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) to install the NVIDIA Container Toolkit, ensuring that your Docker can access the GPU. For users in mainland China who may have difficulty accessing Docker Hub, you can use mirror acceleration services to pull the images. First, run the following command to pull and initialize the container:

```bash
LOCAL_WORKDIR=/path/to/your/workspace
HOST_PORT=8901
CONTAINER_PORT=80
docker run --gpus all --name qwen3-omni \
    -v /var/run/docker.sock:/var/run/docker.sock -p $HOST_PORT:$CONTAINER_PORT \
    --mount type=bind,source=$LOCAL_WORKDIR,target=/data/shared/Qwen3-Omni \
    --shm-size=4gb \
    -it qwenllm/qwen3-omni:3-cu124
```

After executing the command, you will enter the bash shell of the container. Your local model and data directory (**please replace** `/path/to/your/workspace` **with the actual path**) will be mounted to the container's internal path `/data/shared/Qwen3-Omni`. The host's port `8901` is mapped to port `80` in the container, meaning you can access the service inside the container by visiting port `8901` on the host machine.

Please note that services inside the container must be started with the IP `0.0.0.0` to ensure proper port forwarding. For example:

```bash
# Run this command inside the Docker container
python web_demo.py -c Qwen/Qwen3-Omni-30B-A3B-Instruct --server-port 80 --server-name 0.0.0.0
```

For more ways to launch the web demo, please refer to [Launch Local Web UI Demo](#launch-local-web-ui-demo). If you exit the container, you can re-enter it using the following command:

```bash
docker start qwen3-omni
docker exec -it qwen3-omni bash
```

Or if you want to completely remove the container, please run:

```bash
docker rm -f qwen3-omni
```

## Evaluation

### Performance of Qwen3-Omni

Qwen3-Omni maintains state-of-the-art performance on text and visual modalities without degradation relative to same-size single-model Qwen counterparts. Across 36 audio and audio-visual benchmarks, it achieves open-source SOTA on 32 and sets the SOTA on 22, outperforming strong closed-source systems such as Gemini 2.5 Pro and GPT-4o.

<details>
<summary>Text -> Text</summary>

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: left;"></th>
      <th style="text-align: center;">GPT-4o-0327</th>
      <th style="text-align: center;">Qwen3-235B-A22B<br>Non Thinking</th>
      <th style="text-align: center;">Qwen3-30B-A3B-Instruct-2507</th>
      <th style="text-align: center;">Qwen3-Omni-30B-A3B-Instruct</th>
      <th style="text-align: center;">Qwen3-Omni-Flash-Instruct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2" style="text-align: left; vertical-align: middle;">General<br>Tasks</td>
      <td style="text-align: left;">MMLU-Redux</td>
      <td style="text-align: center;"><strong>91.3</strong></td>
      <td style="text-align: center;">89.2</td>
      <td style="text-align: center;">89.3</td>
      <td style="text-align: center;">86.6</td>
      <td style="text-align: center;">86.8</td>
    </tr>
    <tr>
      <td style="text-align: left;">GPQA</td>
      <td style="text-align: center;">66.9</td>
      <td style="text-align: center;">62.9</td>
      <td style="text-align: center;"><strong>70.4</strong></td>
      <td style="text-align: center;">69.6</td>
      <td style="text-align: center;">69.7</td>
    </tr>
    <tr>
      <td rowspan="2" style="text-align: left; vertical-align: middle;">Reasoning</td>
      <td style="text-align: left;">AIME25</td>
      <td style="text-align: center;">26.7</td>
      <td style="text-align: center;">24.7</td>
      <td style="text-align: center;">61.3</td>
      <td style="text-align: center;">65.0</td>
      <td style="text-align: center;"><strong>65.9</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">ZebraLogic</td>
      <td style="text-align: center;">52.6</td>
      <td style="text-align: center;">37.7</td>
      <td style="text-align: center;"><strong>90.0</strong></td>
      <td style="text-align: center;">76.0</td>
      <td style="text-align: center;">76.1</td>
    </tr>
    <tr>
      <td style="text-align: left; vertical-align: middle;">Code</td>
      <td style="text-align: left;">MultiPL-E</td>
      <td style="text-align: center;">82.7</td>
      <td style="text-align: center;">79.3</td>
      <td style="text-align: center;"><strong>83.8</strong></td>
      <td style="text-align: center;">81.4</td>
      <td style="text-align: center;">81.5</td>
    </tr>
  </tbody>
  <tbody>
    <tr style="border-top: 1px solid #ddd;">
      <td rowspan="3" style="text-align: left; vertical-align: middle;">Alignment<br>Tasks</td>
      <td style="text-align: left;">IFEval</td>
      <td style="text-align: center;">83.9</td>
      <td style="text-align: center;">83.2</td>
      <td style="text-align: center;"><strong>84.7</strong></td>
      <td style="text-align: center;">81.0</td>
      <td style="text-align: center;">81.7</td>
    </tr>
    <tr>
      <td style="text-align: left;">Creative Writing v3</td>
      <td style="text-align: center;">84.9</td>
      <td style="text-align: center;">80.4</td>
      <td style="text-align: center;"><strong>86.0</strong></td>
      <td style="text-align: center;">80.6</td>
      <td style="text-align: center;">81.8</td>
    </tr>
    <tr>
      <td style="text-align: left;">WritingBench</td>
      <td style="text-align: center;">75.5</td>
      <td style="text-align: center;">77.0</td>
      <td style="text-align: center;"><strong>85.5</strong></td>
      <td style="text-align: center;">82.6</td>
      <td style="text-align: center;">83.0</td>
    </tr>
    <tr>
      <td style="text-align: left; vertical-align: middle;">Agent</td>
      <td style="text-align: left;">BFCL-v3</td>
      <td style="text-align: center;">66.5</td>
      <td style="text-align: center;"><strong>68.0</strong></td>
      <td style="text-align: center;">65.1</td>
      <td style="text-align: center;">64.4</td>
      <td style="text-align: center;">65.0</td>
    </tr>
    <tr>
      <td rowspan="2" style="text-align: left; vertical-align: middle;">Multilingual<br>Tasks</td>
      <td style="text-align: left;">MultiIF</td>
      <td style="text-align: center;"><strong>70.4</strong></td>
      <td style="text-align: center;">70.2</td>
      <td style="text-align: center;">67.9</td>
      <td style="text-align: center;">64.0</td>
      <td style="text-align: center;">64.7</td>
    </tr>
    <tr>
      <td style="text-align: left;">PolyMATH</td>
      <td style="text-align: center;">25.5</td>
      <td style="text-align: center;">27.0</td>
      <td style="text-align: center;"><strong>43.1</strong></td>
      <td style="text-align: center;">37.9</td>
      <td style="text-align: center;">39.3</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr style="border-bottom: 1px solid black;">
      <th></th>
      <th></th>
      <th>Gemini-2.5-Flash<br>Thinking</th>
      <th>Qwen3-235B-A22B<br>Thinking</th>
      <th>Qwen3-30B-A3B-Thinking-2507</th>
      <th>Qwen3-Omni-30B-A3B-Thinking</th>
      <th>Qwen3-Omni-Flash-Thinking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2"><em>General<br>Tasks</em></td>
      <td>MMLU-Redux</td>
      <td>92.1</td>
      <td><b>92.7</b></td>
      <td>91.4</td>
      <td>88.8</td>
      <td>89.7</td>
    </tr>
    <tr style="border-top: 1px solid #ddd;">
      <td>GPQA</td>
      <td><b>82.8</b></td>
      <td>71.1</td>
      <td>73.4</td>
      <td>73.1</td>
      <td>73.1</td>
    </tr>
    <tr style="border-top: 1px solid black;">
      <td rowspan="2"><em>Reasoning</em></td>
      <td>AIME25</td>
      <td>72.0</td>
      <td>81.5</td>
      <td><b>85.0</b></td>
      <td>73.7</td>
      <td>74.0</td>
    </tr>
    <tr style="border-top: 1px solid #ddd;">
      <td>LiveBench 20241125</td>
      <td>74.3</td>
      <td><b>77.1</b></td>
      <td>76.8</td>
      <td>71.8</td>
      <td>70.3</td>
    </tr>
    <tr style="border-top: 1px solid black;">
      <td><em>Code</em></td>
      <td>MultiPL-E</td>
      <td><b>84.5</b></td>
      <td>79.9</td>
      <td>81.3</td>
      <td>80.6</td>
      <td>81.0</td>
    </tr>
    <tr style="border-top: 1px solid #ddd;">
      <td rowspan="4"><em>Alignment<br>Tasks</em></td>
      <td>IFEval</td>
      <td><b>89.8</b></td>
      <td>83.4</td>
      <td>88.9</td>
      <td>85.1</td>
      <td>85.2</td>
    </tr>
    <tr style="border-top: 1px solid #ddd;">
      <td>Arena-Hard v2</td>
      <td>56.7</td>
      <td><b>61.5</b></td>
      <td>56.0</td>
      <td>55.1</td>
      <td>57.8</td>
    </tr>
    <tr style="border-top: 1px solid #ddd;">
      <td>Creative Writing v3</td>
      <td><b>85.0</b></td>
      <td>84.6</td>
      <td>84.4</td>
      <td>82.5</td>
      <td>83.6</td>
    </tr>
    <tr style="border-top: 1px solid #ddd;">
      <td>WritingBench</td>
      <td>83.9</td>
      <td>80.3</td>
      <td>85.0</td>
      <td>85.5</td>
      <td><b>85.9</b></td>
    </tr>
    <tr style="border-top: 1px solid black;">
      <td><em>Agent</em></td>
      <td>BFCL-v3</td>
      <td>68.6</td>
      <td>70.8</td>
      <td><b>72.4</b></td>
      <td>63.2</td>
      <td>64.5</td>
    </tr>
    <tr style="border-top: 1px solid black;">
      <td rowspan="2"><em>Multilingual<br>Tasks</em></td>
      <td>MultiIF</td>
      <td>74.4</td>
      <td>71.9</td>
      <td><b>76.4</b></td>
      <td>72.9</td>
      <td>73.2</td>
    </tr>
    <tr>
      <td>PolyMATH</td>
      <td>49.8</td>
      <td><b>54.7</b></td>
      <td>52.6</td>
      <td>47.1</td>
      <td>48.7</td>
    </tr>
  </tbody>
</table>

</details>

<details>
<summary>Audio -> Text</summary>

<table style="width:100%; border-collapse: collapse;">
<thead>
  <tr>
    <th align="left" style="padding: 8px;"></th>
    <th align="center" style="padding: 8px;">Seed-ASR</th>
    <th align="center" style="padding: 8px;">Voxtral-Mini</th>
    <th align="center" style="padding: 8px;">Voxtral-Small</th>
    <th align="center" style="padding: 8px;">GPT-4o-Transcribe</th>
    <th align="center" style="padding: 8px;">Gemini-2.5-Pro</th>
    <th align="center" style="padding: 8px;">Qwen2.5-Omni</th>
    <th align="center" style="padding: 8px;">Qwen3-Omni-30B-A3B-Instruct</th>
    <th align="center" style="padding: 8px;">Qwen3-Omni-Flash-Instruct</th>
  </tr>
</thead>
<tbody>
  <tr style="border-top: 1px solid #333;">
    <td colspan="9" align="center"; style="border-top: 1px solid black; border-bottom: 1px solid black;"><em>EN & ZH ASR (wer)</em></td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Wenetspeech<br><em>net</em> | <em>meeting</em></td>
    <td align="center" style="padding: 8px;">4.66 | <strong>5.69</strong></td>
    <td align="center" style="padding: 8px;">24.30 | 31.53</td>
    <td align="center" style="padding: 8px;">20.33 | 26.08</td>
    <td align="center" style="padding: 8px;">15.30 | 32.27</td>
    <td align="center" style="padding: 8px;">14.43 | 13.47</td>
    <td align="center" style="padding: 8px;">5.91 | 7.65</td>
    <td align="center" style="padding: 8px;">4.69 | 5.89</td>
    <td align="center" style="padding: 8px;"><strong>4.62</strong> | 5.75</td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Librispeech<br><em>clean</em> | <em>other</em></td>
    <td align="center" style="padding: 8px;">1.58 | 2.84</td>
    <td align="center" style="padding: 8px;">1.88 | 4.12</td>
    <td align="center" style="padding: 8px;">1.56 | 3.30</td>
    <td align="center" style="padding: 8px;">1.39 | 3.75</td>
    <td align="center" style="padding: 8px;">2.89 | 3.56</td>
    <td align="center" style="padding: 8px;">1.74 | 3.45</td>
    <td align="center" style="padding: 8px;"><strong>1.22</strong> | 2.48</td>
    <td align="center" style="padding: 8px;">1.27 | <strong>2.44</strong></td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">CV15-en</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;">9.47</td>
    <td align="center" style="padding: 8px;">7.79</td>
    <td align="center" style="padding: 8px;">10.01</td>
    <td align="center" style="padding: 8px;">9.89</td>
    <td align="center" style="padding: 8px;">7.61</td>
    <td align="center" style="padding: 8px;">6.05</td>
    <td align="center" style="padding: 8px;"><strong>5.94</strong></td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">CV15-zh</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;">24.67</td>
    <td align="center" style="padding: 8px;">19.30</td>
    <td align="center" style="padding: 8px;">9.84</td>
    <td align="center" style="padding: 8px;">8.00</td>
    <td align="center" style="padding: 8px;">5.13</td>
    <td align="center" style="padding: 8px;">4.31</td>
    <td align="center" style="padding: 8px;"><strong>4.28</strong></td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Fleurs-en</td>
    <td align="center" style="padding: 8px;">3.40</td>
    <td align="center" style="padding: 8px;">3.96</td>
    <td align="center" style="padding: 8px;">3.77</td>
    <td align="center" style="padding: 8px;">3.32</td>
    <td align="center" style="padding: 8px;">2.94</td>
    <td align="center" style="padding: 8px;">3.77</td>
    <td align="center" style="padding: 8px;"><strong>2.72</strong></td>
    <td align="center" style="padding: 8px;">2.74</td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Fleurs-zh</td>
    <td align="center" style="padding: 8px;">2.69</td>
    <td align="center" style="padding: 8px;">12.22</td>
    <td align="center" style="padding: 8px;">7.98</td>
    <td align="center" style="padding: 8px;">2.44</td>
    <td align="center" style="padding: 8px;">2.71</td>
    <td align="center" style="padding: 8px;">2.54</td>
    <td align="center" style="padding: 8px;">2.20</td>
    <td align="center" style="padding: 8px;"><strong>2.19</strong></td>
  </tr>
  <tr style="border-top: 1px solid #333;">
    <td colspan="9" align="center"; style="border-top: 1px solid black; border-bottom: 1px solid black;"><em>Multilingual ASR (wer)</em></td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Fleurs-avg<br>(19 lang)</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;">15.67</td>
    <td align="center" style="padding: 8px;">8.09</td>
    <td align="center" style="padding: 8px;">4.48</td>
    <td align="center" style="padding: 8px;">5.55</td>
    <td align="center" style="padding: 8px;">14.04</td>
    <td align="center" style="padding: 8px;">5.33</td>
    <td align="center" style="padding: 8px;"><strong>5.31</strong></td>
  </tr>
  <tr style="border-top: 1px solid #333;">
    <td colspan="9" align="center"; style="border-top: 1px solid black; border-bottom: 1px solid black;"><em>Lyric ASR (wer)</em></td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">MIR-1K (vocal-only)</td>
    <td align="center" style="padding: 8px;">6.45</td>
    <td align="center" style="padding: 8px;">23.33</td>
    <td align="center" style="padding: 8px;">18.73</td>
    <td align="center" style="padding: 8px;">11.87</td>
    <td align="center" style="padding: 8px;">9.85</td>
    <td align="center" style="padding: 8px;">8.15</td>
    <td align="center" style="padding: 8px;">5.90</td>
    <td align="center" style="padding: 8px;"><strong>5.85</strong></td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Opencpop-test</td>
    <td align="center" style="padding: 8px;">2.98</td>
    <td align="center" style="padding: 8px;">31.01</td>
    <td align="center" style="padding: 8px;">16.06</td>
    <td align="center" style="padding: 8px;">7.93</td>
    <td align="center" style="padding: 8px;">6.49</td>
    <td align="center" style="padding: 8px;">2.84</td>
    <td align="center" style="padding: 8px;"><strong>1.54</strong></td>
    <td align="center" style="padding: 8px;">2.02</td>
  </tr>
  <tr style="border-top: 1px solid #333;">
    <td colspan="9" align="center"; style="border-top: 1px solid black; border-bottom: 1px solid black;"><em>S2TT (BLEU)</em></td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Fleurs-en2xx</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;">30.35</td>
    <td align="center" style="padding: 8px;">37.85</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;"><strong>39.25</strong></td>
    <td align="center" style="padding: 8px;">29.22</td>
    <td align="center" style="padding: 8px;">37.50</td>
    <td align="center" style="padding: 8px;">36.22</td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Fleurs-xx2en</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;">27.54</td>
    <td align="center" style="padding: 8px;">32.81</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;"><strong>35.41</strong></td>
    <td align="center" style="padding: 8px;">28.61</td>
    <td align="center" style="padding: 8px;">31.08</td>
    <td align="center" style="padding: 8px;">30.71</td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Fleurs-zh2xx</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;">17.03</td>
    <td align="center" style="padding: 8px;">22.05</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;"><strong>26.63</strong></td>
    <td align="center" style="padding: 8px;">17.97</td>
    <td align="center" style="padding: 8px;">25.17</td>
    <td align="center" style="padding: 8px;">25.10</td>
  </tr>
  <tr>
    <td align="left" style="padding: 8px;">Fleurs-xx2zh</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;">28.75</td>
    <td align="center" style="padding: 8px;">34.82</td>
    <td align="center" style="padding: 8px;">-</td>
    <td align="center" style="padding: 8px;"><strong>37.50</strong></td>
    <td align="center" style="padding: 8px;">27.68</td>
    <td align="center" style="padding: 8px;">33.13</td>
    <td align="center" style="padding: 8px;">31.19</td>
  </tr>
</tbody>
</table>

<table style="width:100%; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 1px solid #ddd;">
      <th style="text-align:left; padding: 8px;"></th>
      <th style="text-align:center; padding: 8px;">GPT-4o-Audio</th>
      <th style="text-align:center; padding: 8px;">Gemini-2.5-Flash</th>
      <th style="text-align:center; padding: 8px;">Gemini-2.5-Pro</th>
      <th style="text-align:center; padding: 8px;">Qwen2.5-Omni</th>
      <th style="text-align:center; padding: 8px;">Qwen3-Omni-30B-A3B-Instruct</th>
      <th style="text-align:center; padding: 8px;">Qwen3-Omni-30B-A3B-Thinking</th>
      <th style="text-align:center; padding: 8px;">Qwen3-Omni-Flash-Instruct</th>
      <th style="text-align:center; padding: 8px;">Qwen3-Omni-Flash-Thinking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="9" align="center" style="padding: 8px; font-weight: bold; border-top: 1px solid black; border-bottom: 1px solid black;"><strong>VoiceBench</strong></td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">AlpacaEval</td>
      <td style="text-align:center; padding: 8px;">95.6</td>
      <td style="text-align:center; padding: 8px;">96.1</td>
      <td style="text-align:center; padding: 8px;">94.3</td>
      <td style="text-align:center; padding: 8px;">89.9</td>
      <td style="text-align:center; padding: 8px;">94.8</td>
      <td style="text-align:center; padding: 8px;">96.4</td>
      <td style="text-align:center; padding: 8px;">95.4</td>
      <td style="text-align:center; padding: 8px;"><strong>96.8</strong></td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">CommonEval</td>
      <td style="text-align:center; padding: 8px;">89.8</td>
      <td style="text-align:center; padding: 8px;">88.3</td>
      <td style="text-align:center; padding: 8px;">88.4</td>
      <td style="text-align:center; padding: 8px;">76.7</td>
      <td style="text-align:center; padding: 8px;">90.8</td>
      <td style="text-align:center; padding: 8px;">90.5</td>
      <td style="text-align:center; padding: 8px;"><strong>91.0</strong></td>
      <td style="text-align:center; padding: 8px;">90.9</td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">WildVoice</td>
      <td style="text-align:center; padding: 8px;">91.6</td>
      <td style="text-align:center; padding: 8px;">92.1</td>
      <td style="text-align:center; padding: 8px;">93.4</td>
      <td style="text-align:center; padding: 8px;">77.7</td>
      <td style="text-align:center; padding: 8px;">91.6</td>
      <td style="text-align:center; padding: 8px;">90.5</td>
      <td style="text-align:center; padding: 8px;"><strong>92.3</strong></td>
      <td style="text-align:center; padding: 8px;">90.9</td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">SD-QA</td>
      <td style="text-align:center; padding: 8px;">75.5</td>
      <td style="text-align:center; padding: 8px;">84.5</td>
      <td style="text-align:center; padding: 8px;"><strong>90.1</strong></td>
      <td style="text-align:center; padding: 8px;">56.4</td>
      <td style="text-align:center; padding: 8px;">76.9</td>
      <td style="text-align:center; padding: 8px;">78.1</td>
      <td style="text-align:center; padding: 8px;">76.8</td>
      <td style="text-align:center; padding: 8px;">78.5</td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">MMSU</td>
      <td style="text-align:center; padding: 8px;">80.3</td>
      <td style="text-align:center; padding: 8px;">66.1</td>
      <td style="text-align:center; padding: 8px;">71.1</td>
      <td style="text-align:center; padding: 8px;">61.7</td>
      <td style="text-align:center; padding: 8px;">68.1</td>
      <td style="text-align:center; padding: 8px;">83.0</td>
      <td style="text-align:center; padding: 8px;">68.4</td>
      <td style="text-align:center; padding: 8px;"><strong>84.3</strong></td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">OpenBookQA</td>
      <td style="text-align:center; padding: 8px;">89.2</td>
      <td style="text-align:center; padding: 8px;">56.9</td>
      <td style="text-align:center; padding: 8px;">92.3</td>
      <td style="text-align:center; padding: 8px;">80.9</td>
      <td style="text-align:center; padding: 8px;">89.7</td>
      <td style="text-align:center; padding: 8px;">94.3</td>
      <td style="text-align:center; padding: 8px;">91.4</td>
      <td style="text-align:center; padding: 8px;"><strong>95.0</strong></td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">BBH</td>
      <td style="text-align:center; padding: 8px;">84.1</td>
      <td style="text-align:center; padding: 8px;">83.9</td>
      <td style="text-align:center; padding: 8px;"><strong>92.6</strong></td>
      <td style="text-align:center; padding: 8px;">66.7</td>
      <td style="text-align:center; padding: 8px;">80.4</td>
      <td style="text-align:center; padding: 8px;">88.9</td>
      <td style="text-align:center; padding: 8px;">80.6</td>
      <td style="text-align:center; padding: 8px;">89.6</td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">IFEval</td>
      <td style="text-align:center; padding: 8px;">76.0</td>
      <td style="text-align:center; padding: 8px;">83.8</td>
      <td style="text-align:center; padding: 8px;"><strong>85.7</strong></td>
      <td style="text-align:center; padding: 8px;">53.5</td>
      <td style="text-align:center; padding: 8px;">77.8</td>
      <td style="text-align:center; padding: 8px;">80.6</td>
      <td style="text-align:center; padding: 8px;">75.2</td>
      <td style="text-align:center; padding: 8px;">80.8</td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">AdvBench</td>
      <td style="text-align:center; padding: 8px;">98.7</td>
      <td style="text-align:center; padding: 8px;">98.9</td>
      <td style="text-align:center; padding: 8px;">98.1</td>
      <td style="text-align:center; padding: 8px;">99.2</td>
      <td style="text-align:center; padding: 8px;"><strong>99.3</strong></td>
      <td style="text-align:center; padding: 8px;">97.2</td>
      <td style="text-align:center; padding: 8px;"><strong>99.4</strong></td>
      <td style="text-align:center; padding: 8px;">98.9</td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">Overall</td>
      <td style="text-align:center; padding: 8px;">86.8</td>
      <td style="text-align:center; padding: 8px;">83.4</td>
      <td style="text-align:center; padding: 8px;"><strong>89.6</strong></td>
      <td style="text-align:center; padding: 8px;">73.6</td>
      <td style="text-align:center; padding: 8px;">85.5</td>
      <td style="text-align:center; padding: 8px;">88.8</td>
      <td style="text-align:center; padding: 8px;">85.6</td>
      <td style="text-align:center; padding: 8px;">89.5</td>
    </tr>
    <tr>
      <td colspan="9" align="center" style="padding: 8px; font-weight: bold; border-top: 1px solid black; border-bottom: 1px solid black;"><strong>Audio Reasoning</strong></td>
    </tr>
    <tr>
      <td style="text-align:left; padding: 8px;">MMAU-v05.15.25</td>
      <td style="text-align:center; padding: 8px;">62.5</td>
      <td style="text-align:center; padding: 8px;">71.8</td>
      <td style="text-align:center; padding: 8px;">77.4</td>
      <td style="text-align:center; padding: 8px;">65.5</td>
      <td style="text-align:center; padding: 8px;">77.5</td>
      <td style="text-align:center; padding: 8px;">75.4</td>
      <td style="text-align:center; padding: 8px;"><strong>77.6</strong></td>
      <td style="text-align:center; padding: 8px;">76.5</td>
    </tr>
    <tr">
      <td style="text-align:left; padding: 8px;">MMSU</td>
      <td style="text-align:center; padding: 8px;">56.4</td>
      <td style="text-align:center; padding: 8px;">70.2</td>
      <td style="text-align:center; padding: 8px;"><strong>77.7</strong></td>
      <td style="text-align:center; padding: 8px;">62.6</td>
      <td style="text-align:center; padding: 8px;">69.0</td>
      <td style="text-align:center; padding: 8px;">70.2</td>
      <td style="text-align:center; padding: 8px;">69.1</td>
      <td style="text-align:center; padding: 8px;">71.3</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr style="border-bottom: 1px solid black;">
      <th style="text-align: left;"></th>
      <th style="text-align: center;">Best Specialist<br>Models</th>
      <th style="text-align: center;">GPT-4o-Audio</th>
      <th style="text-align: center;">Gemini-2.5-Pro</th>
      <th style="text-align: center;">Qwen2.5-Omni</th>
      <th style="text-align: center;">Qwen3-Omni-30B-A3B-Instruct</th>
      <th style="text-align: center;">Qwen3-Omni-Flash-Instruct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left;">RUL-MuchoMusic</td>
      <td style="text-align: center;">47.6 (Audio Flamingo 3)</td>
      <td style="text-align: center;">36.1</td>
      <td style="text-align: center;">49.4</td>
      <td style="text-align: center;">47.3</td>
      <td style="text-align: center;">52.0</td>
      <td style="text-align: center;"><strong>52.1</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">GTZAN<br><em>Acc.</em></td>
      <td style="text-align: center;">87.9 (CLaMP 3)</td>
      <td style="text-align: center;">76.5</td>
      <td style="text-align: center;">81.0</td>
      <td style="text-align: center;">81.7</td>
      <td style="text-align: center;">93.0</td>
      <td style="text-align: center;"><strong>93.1</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">MTG Genre<br><em>Micro F1</em></td>
      <td style="text-align: center;">35.8 (MuQ-MuLan)</td>
      <td style="text-align: center;">25.3</td>
      <td style="text-align: center;">32.6</td>
      <td style="text-align: center;">32.5</td>
      <td style="text-align: center;">39.0</td>
      <td style="text-align: center;"><strong>39.5</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">MTG Mood/Theme<br><em>Micro F1</em></td>
      <td style="text-align: center;">10.9 (MuQ-MuLan)</td>
      <td style="text-align: center;">11.3</td>
      <td style="text-align: center;">14.1</td>
      <td style="text-align: center;">8.9</td>
      <td style="text-align: center;">21.0</td>
      <td style="text-align: center;"><strong>21.7</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">MTG Instrument<br><em>Micro F1</em></td>
      <td style="text-align: center;">39.8 (MuQ-MuLan)</td>
      <td style="text-align: center;">34.2</td>
      <td style="text-align: center;">33.0</td>
      <td style="text-align: center;">22.6</td>
      <td style="text-align: center;">40.5</td>
      <td style="text-align: center;"><strong>40.7</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">MTG Top50<br><em>Micro F1</em></td>
      <td style="text-align: center;">33.2 (MuQ-MuLan)</td>
      <td style="text-align: center;">25.0</td>
      <td style="text-align: center;">26.1</td>
      <td style="text-align: center;">21.6</td>
      <td style="text-align: center;">36.7</td>
      <td style="text-align: center;"><strong>36.9</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">MagnaTagATune<br><em>Micro F1</em></td>
      <td style="text-align: center;">41.6 (MuQ)</td>
      <td style="text-align: center;">29.2</td>
      <td style="text-align: center;">28.1</td>
      <td style="text-align: center;">30.1</td>
      <td style="text-align: center;">44.3</td>
      <td style="text-align: center;"><strong>46.8</strong></td>
    </tr>
  </tbody>
</table>

</details>

<details>
<summary>Vision -> Text</summary>

<table style="width:100%; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 1px solid black;">
      <th style="text-align: left;">Datasets</th>
      <th style="text-align: center;">GPT4-o</th>
      <th style="text-align: center;">Gemini-2.0-Flash</th>
      <th style="text-align: center;">Qwen2.5-VL<br>72B</th>
      <th style="text-align: center;">Qwen3-Omni-30B-A3B<br>-Instruct</th>
      <th style="text-align: center;">Qwen3-Omni-Flash<br>-Instruct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="6" align="center" style="font-weight: bold; border-top: 1px solid #ddd; border-bottom: 1px solid black;">General Visual Question Answering</td>
    </tr>
    <tr>
      <td style="text-align: left;">MMStar</td>
      <td style="text-align: center;">64.7</td>
      <td style="text-align: center;"><strong>71.4</strong></td>
      <td style="text-align: center;">70.8</td>
      <td style="text-align: center;">68.5</td>
      <td style="text-align: center;">69.3</td>
    </tr>
    <tr>
      <td style="text-align: left;">HallusionBench</td>
      <td style="text-align: center;">55.0</td>
      <td style="text-align: center;">56.3</td>
      <td style="text-align: center;">55.2</td>
      <td style="text-align: center;"><strong>59.7</strong></td>
      <td style="text-align: center;">58.5</td>
    </tr>
    <tr>
      <td style="text-align: left;">MM-MT-Bench</td>
      <td style="text-align: center;"><strong>7.7</strong></td>
      <td style="text-align: center;">6.7</td>
      <td style="text-align: center;">7.6</td>
      <td style="text-align: center;">7.4</td>
      <td style="text-align: center;">7.6</td>
    </tr>
    <tr>
      <td colspan="6" align="center" style="font-weight: bold; border-top: 1px solid black; border-bottom: 1px solid black;">Math & STEM</td>
    </tr>
    <tr>
      <td style="text-align: left;">MMMU_val</td>
      <td style="text-align: center;">69.1</td>
      <td style="text-align: center;"><strong>71.3</strong></td>
      <td style="text-align: center;">70.2</td>
      <td style="text-align: center;">69.1</td>
      <td style="text-align: center;">69.8</td>
    </tr>
    <tr>
      <td style="text-align: left;">MMMU_pro</td>
      <td style="text-align: center;">51.9</td>
      <td style="text-align: center;">56.1</td>
      <td style="text-align: center;">51.1</td>
      <td style="text-align: center;">57.0</td>
      <td style="text-align: center;"><strong>57.6</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">MathVista_mini</td>
      <td style="text-align: center;">63.8</td>
      <td style="text-align: center;">71.4</td>
      <td style="text-align: center;">74.8</td>
      <td style="text-align: center;">75.9</td>
      <td style="text-align: center;"><strong>77.4</strong></td>
    </tr>
    <tr>
      <td style="text-align: left;">MathVision_full</td>
      <td style="text-align: center;">30.4</td>
      <td style="text-align: center;">48.6</td>
      <td style="text-align: center;">38.1</td>
      <td style="text-align: center;">56.3</td>
      <td style="text-align: center;"><strong>58.3</strong></td>
    </tr>
    <tr>
      <td colspan="6" align="center" style="font-weight: bold; border-top: 1px solid black; border-bottom: 1px solid black;">Documentation Understanding</td>
    </tr>
    <tr>
      <td style="text-align: left;">AI2D</td>
      <td style="text-align: center;">84.6</td>
      <td style="text-align: center;">86.7</td>
      <td style="text-align: center;"><strong>88.7</strong></td>
      <td style="text-align: center;">85.2</td>
      <td style="text-align: center;">86.4</td>
    </tr>
    <tr>
      <td style="text-align: left;">ChartQA_test</td>
      <td style="text-align: center;">86.7</td>
      <td style="text-align: center;">64.6</td>
      <td style="text-align: center;"><strong>89.5</strong></td>
      <td style="text-align: center;">86.8</td>
      <td style="text-align: center;">87.1</td>
    </tr>
    <tr>
      <td colspan="6" align="center" style="font-weight: bold; border-top: 1px solid black; border-bottom: 1px solid black;">Counting</td>
    </tr>
    <tr>
      <td style="text-align: left;">CountBench</td>
      <td style="text-align: center;">87.9</td>
      <td style="text-align: center;">91.2</td>
      <td style="text-align: center;"><strong>93.6</strong></td>
      <td style="text-align: center;">90.0</td>
      <td style="text-align: center;">90.0</td>
    </tr>
    <tr>
      <td colspan="6" align="center" style="font-weight: bold; border-top: 1px solid black; border-bottom: 1px solid black;">Video Understanding</td>
    </tr>
    <tr>
      <td style="text-align: left;">Video-MME</td>
      <td style="text-align: center;">71.9</td>
      <td style="text-align: center;">72.4</td>
      <td style="text-align: center;"><strong>73.3</strong></td>
      <td style="text-align: center;">70.5</td>
      <td style="text-align: center;">71.4</td>
    </tr>
    <tr>
      <td style="text-align: left;">LVBench</td>
      <td style="text-align: center;">30.8</td>
      <td style="text-align: center;"><strong>57.9</strong></td>
      <td style="text-align: center;">47.3</td>
      <td style="text-align: center;">50.2</td>
      <td style="text-align: center;">51.1</td>
    </tr>
    <tr>
      <td style="text-align: left;">MLVU</td>
      <td style="text-align: center;">64.6</td>
      <td style="text-align: center;">71.0</td>
      <td style="text-align: center;">74.6</td>
      <td style="text-align: center;">75.2</td>
      <td style="text-align: center;"><strong>75.5</strong></td>
    </tr>
  </tbody>
</table>

<table style="width: 100%; border-collapse: collapse;">
  <thead style="border-bottom: 1px solid black;">
    <tr>
      <th align="left" style="padding: 6px;">Datasets</th>
      <th align="center" style="padding: 6px;">Gemini-2.5-flash-thinking</th>
      <th align="center" style="padding: 6px;">InternVL-3.5-241B-A28B</th>
      <th align="center" style="padding: 6px;">Qwen3-Omni-30B-A3B-Thinking</th>
      <th align="center" style="padding: 6px;">Qwen3-Omni-Flash-Thinking</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-top: 2px solid black; border-bottom: 1px solid #ccc;">
      <td colspan="5" align="center" style="padding: 6px 0; font-weight: bold; border-bottom: 1px solid black;">General Visual Question Answering</td>
    </tr>
    <tr>
      <td style="padding: 6px;">MMStar</td>
      <td align="center" style="padding: 6px;">75.5</td>
      <td align="center" style="padding: 6px;"><b>77.9</b></td>
      <td align="center" style="padding: 6px;">74.9</td>
      <td align="center" style="padding: 6px;">75.5</td>
    </tr>
    <tr>
      <td style="padding: 6px;">HallusionBench</td>
      <td align="center" style="padding: 6px;">61.1</td>
      <td align="center" style="padding: 6px;">57.3</td>
      <td align="center" style="padding: 6px;">62.8</td>
      <td align="center" style="padding: 6px;"><b>63.4</b></td>
    </tr>
    <tr>
      <td style="padding: 6px;">MM-MT-Bench</td>
      <td align="center" style="padding: 6px;">7.8</td>
      <td align="center" style="padding: 6px;">–</td>
      <td align="center" style="padding: 6px;"><b>8.0</b></td>
      <td align="center" style="padding: 6px;"><b>8.0</b></td>
    </tr>
    <tr style="border-top: 1px solid black; border-bottom: 1px solid #ccc;">
      <td colspan="5" align="center" style="padding: 6px 0; font-weight: bold; border-top: 1px solid black;  border-bottom: 1px solid black;">Math & STEM</td>
    </tr>
    <tr>
      <td style="padding: 6px;">MMMU_val</td>
      <td align="center" style="padding: 6px;">76.9</td>
      <td align="center" style="padding: 6px;"><b>77.7</b></td>
      <td align="center" style="padding: 6px;">75.6</td>
      <td align="center" style="padding: 6px;">75.0</td>
    </tr>
    <tr>
      <td style="padding: 6px;">MMMU_pro</td>
      <td align="center" style="padding: 6px;"><b>65.8</b></td>
      <td align="center" style="padding: 6px;">–</td>
      <td align="center" style="padding: 6px;">60.5</td>
      <td align="center" style="padding: 6px;">60.8</td>
    </tr>
    <tr>
      <td style="padding: 6px;">MathVista_mini</td>
      <td align="center" style="padding: 6px;">77.6</td>
      <td align="center" style="padding: 6px;"><b>82.7</b></td>
      <td align="center" style="padding: 6px;">80.0</td>
      <td align="center" style="padding: 6px;">81.2</td>
    </tr>
    <tr>
      <td style="padding: 6px;">MathVision_full</td>
      <td align="center" style="padding: 6px;">62.3</td>
      <td align="center" style="padding: 6px;"><b>63.9</b></td>
      <td align="center" style="padding: 6px;">62.9</td>
      <td align="center" style="padding: 6px;">63.8</td>
    </tr>
    <tr style="border-top: 1px solid black; border-bottom: 1px solid #ccc;">
      <td colspan="5" align="center" style="padding: 6px 0; font-weight: bold; border-top: 1px solid black;  border-bottom: 1px solid black;">Documentation Understanding</td>
    </tr>
    <tr>
      <td style="padding: 6px;">AI2D_test</td>
      <td align="center" style="padding: 6px;"><b>88.6</b></td>
      <td align="center" style="padding: 6px;">87.3</td>
      <td align="center" style="padding: 6px;">86.1</td>
      <td align="center" style="padding: 6px;">86.8</td>
    </tr>
    <tr>
      <td style="padding: 6px;">ChartQA_test</td>
      <td align="center" style="padding: 6px;">–</td>
      <td align="center" style="padding: 6px;">88.0</td>
      <td align="center" style="padding: 6px;"><b>89.5</b></td>
      <td align="center" style="padding: 6px;">89.3</td>
    </tr>
    <tr style="border-top: 1px solid black; border-bottom: 1px solid #ccc;">
      <td colspan="5" align="center" style="padding: 6px 0; font-weight: bold; border-top: 1px solid black;  border-bottom: 1px solid black;">Counting</td>
    </tr>
    <tr>
      <td style="padding: 6px;">CountBench</td>
      <td align="center" style="padding: 6px;">88.6</td>
      <td align="center" style="padding: 6px;">–</td>
      <td align="center" style="padding: 6px;">88.6</td>
      <td align="center" style="padding: 6px;"><b>92.5</b></td>
    </tr>
    <tr style="border-top: 1px solid black; border-bottom: 1px solid #ccc;">
      <td colspan="5" align="center" style="padding: 6px 0; font-weight: bold; border-top: 1px solid black;  border-bottom: 1px solid black;">Video Understanding</td>
    </tr>
    <tr>
      <td style="padding: 6px;">Video-MME</td>
      <td align="center" style="padding: 6px;"><b>79.6</b></td>
      <td align="center" style="padding: 6px;">72.9</td>
      <td align="center" style="padding: 6px;">69.7</td>
      <td align="center" style="padding: 6px;">69.8</td>
    </tr>
    <tr>
      <td style="padding: 6px;">LVBench</td>
      <td align="center" style="padding: 6px;"><b>64.5</b></td>
      <td align="center" style="padding: 6px;">–</td>
      <td align="center" style="padding: 6px;">49.0</td>
      <td align="center" style="padding: 6px;">49.5</td>
    </tr>
    <tr>
      <td style="padding: 6px;">MLVU</td>
      <td align="center" style="padding: 6px;"><b>82.1</b></td>
      <td align="center" style="padding: 6px;">78.2</td>
      <td align="center" style="padding: 6px;">72.9</td>
      <td align="center" style="padding: 6px;">73.9</td>
    </tr>
  </tbody>
</table>

</details>

<details>
<summary>AudioVisual -> Text</summary>

<table>
  <thead>
    <tr>
      <th>Datasets</th>
      <th>Previous Open-source SoTA</th>
      <th>Gemini-2.5-Flash</th>
      <th>Qwen2.5-Omni</th>
      <th>Qwen3-Omni-30B-A3B-Instruct</th>
      <th>Qwen3-Omni-Flash-Instruct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WorldSense</td>
      <td>47.1</td>
      <td>50.9</td>
      <td>45.4</td>
      <td>54.0</td>
      <td><strong>54.1</strong></td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Datasets</th>
      <th>Previous Open-source SoTA</th>
      <th>Gemini-2.5-Flash-Thinking</th>
      <th>Qwen3-Omni-30B-A3B-Thinking</th>
      <th>Qwen3-Omni-Flash-Thinking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DailyOmni</td>
      <td>69.8</td>
      <td>72.7</td>
      <td>75.8</b></td>
      <td><b>76.2</td>
    </tr>
    <tr>
      <td>VideoHolmes</td>
      <td>55.6</td>
      <td>49.5</td>
      <td><b>57.3</b></td>
      <td><b>57.3</b></td>
    </tr>
  </tbody>
</table>

</details>


<details>
<summary>Zero-shot Speech Generation</summary>

<table>
  <thead>
    <tr>
      <th align="left">Datasets</th>
      <th align="left">Model</th>
      <th align="left">Performance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&nbsp;</td>
      <td colspan="2" align="center"><em>Content Consistency</em></td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td rowspan="10" align="center" valign="middle"><strong>SEED</strong><br><em>test-zh</em> | <em>test-en</em></td>
      <td align="left">Seed-TTS<sub>ICL</sub></td>
      <td align="left">1.11 | 2.24</td>
    </tr>
    <tr>
      <td align="left">Seed-TTS<sub>RL</sub></td>
      <td align="left">1.00 | 1.94</td>
    </tr>
    <tr>
      <td align="left">MaskGCT</td>
      <td align="left">2.27 | 2.62</td>
    </tr>
    <tr>
      <td align="left">E2 TTS</td>
      <td align="left">1.97 | 2.19</td>
    </tr>
    <tr>
      <td align="left">F5-TTS</td>
      <td align="left">1.56 | 1.83</td>
    </tr>
    <tr>
      <td align="left">Spark TTS</td>
      <td align="left">1.20 | 1.98</td>
    </tr>
    <tr>
      <td align="left">CosyVoice 2</td>
      <td align="left">1.45 | 2.57</td>
    </tr>
    <tr>
      <td align="left">CosyVoice 3</td>
      <td align="left"><strong>0.71</strong> | 1.45</td>
    </tr>
    <tr>
      <td align="left">Qwen2.5-Omni-7B</td>
      <td align="left">1.42 | 2.33</td>
    </tr>
    <tr>
      <td align="left">Qwen3-Omni-30B-A3B</td>
      <td align="left">1.07 | <strong>1.39</strong></td>
    </tr>
  </tbody>
</table>

</details>

<details>
<summary>Multilingual Speech Generation </summary>

<table>
  <thead>
    <tr>
      <th rowspan="2" align="left">Language</th>
      <th colspan="3" style="text-align:center; padding: 8px; font-weight: bold; border-bottom: 1px solid #ddd;">Content Consistency</th>
      <th colspan="3"  style="text-align:center; padding: 8px; font-weight: bold; border-bottom: 1px solid #ddd;">Speaker Similarity</th>
    </tr>
    <tr>
      <th align="center">Qwen3-Omni-30B-A3B</th>
      <th align="center">MiniMax</th>
      <th align="center">ElevenLabs</th>
      <th align="center">Qwen3-Omni-30B-A3B</th>
      <th align="center">MiniMax</th>
      <th align="center">ElevenLabs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">Chinese</td>
      <td align="center"><strong>0.716</strong></td>
      <td align="center">2.252</td>
      <td align="center">16.026</td>
      <td align="center">0.772</td>
      <td align="center"><strong>0.780</strong></td>
      <td align="center">0.677</td>
    </tr>
    <tr>
      <td align="left">English</td>
      <td align="center"><strong>1.069</strong></td>
      <td align="center">2.164</td>
      <td align="center">2.339</td>
      <td align="center"><strong>0.773</strong></td>
      <td align="center">0.756</td>
      <td align="center">0.613</td>
    </tr>
    <tr>
      <td align="left">German</td>
      <td align="center">0.777</td>
      <td align="center">1.906</td>
      <td align="center"><strong>0.572</strong></td>
      <td align="center"><strong>0.738</strong></td>
      <td align="center">0.733</td>
      <td align="center">0.614</td>
    </tr>
    <tr>
      <td align="left">Italian</td>
      <td align="center"><strong>1.067</strong></td>
      <td align="center">1.543</td>
      <td align="center">1.743</td>
      <td align="center"><strong>0.742</strong></td>
      <td align="center">0.699</td>
      <td align="center">0.579</td>
    </tr>
    <tr>
      <td align="left">Portuguese</td>
      <td align="center">1.872</td>
      <td align="center">1.877</td>
      <td align="center"><strong>1.331</strong></td>
      <td align="center">0.770</td>
      <td align="center"><strong>0.805</strong></td>
      <td align="center">0.711</td>
    </tr>
    <tr>
      <td align="left">Spanish</td>
      <td align="center">1.765</td>
      <td align="center"><strong>1.029</strong></td>
      <td align="center">1.084</td>
      <td align="center">0.744</td>
      <td align="center"><strong>0.762</strong></td>
      <td align="center">0.615</td>
    </tr>
    <tr>
      <td align="left">Japanese</td>
      <td align="center">3.631</td>
      <td align="center"><strong>3.519</strong></td>
      <td align="center">10.646</td>
      <td align="center">0.763</td>
      <td align="center"><strong>0.776</strong></td>
      <td align="center">0.738</td>
    </tr>
    <tr>
      <td align="left">Korean</td>
      <td align="center"><strong>1.670</strong></td>
      <td align="center">1.747</td>
      <td align="center">1.865</td>
      <td align="center"><strong>0.778</strong></td>
      <td align="center">0.776</td>
      <td align="center">0.700</td>
    </tr>
    <tr>
      <td align="left">French</td>
      <td align="center"><strong>2.505</strong></td>
      <td align="center">4.099</td>
      <td align="center">5.216</td>
      <td align="center"><strong>0.689</strong></td>
      <td align="center">0.628</td>
      <td align="center">0.535</td>
    </tr>
    <tr>
      <td align="left">Russian</td>
      <td align="center">3.986</td>
      <td align="center">4.281</td>
      <td align="center"><strong>3.878</strong></td>
      <td align="center">0.759</td>
      <td align="center"><strong>0.761</strong></td>
      <td align="center">0.676</td>
    </tr>
  </tbody>
</table>

</details>

<details>
<summary>Cross-Lingual Speech Generation </summary>

<table>
  <thead>
    <tr>
      <th style="text-align: left;">Language</th>
      <th style="text-align: left;">Qwen3-Omni-30B-A3B</th>
      <th style="text-align: left;">CosyVoice3</th>
      <th style="text-align: left;">CosyVoice2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left;">en-to-zh</td>
      <td style="text-align: left;">5.37</td>
      <td style="text-align: left;"><strong>5.09</strong></td>
      <td style="text-align: left;">13.5</td>
    </tr>
    <tr>
      <td style="text-align: left;">ja-to-zh</td>
      <td style="text-align: left;">3.32</td>
      <td style="text-align: left;"><strong>3.05</strong></td>
      <td style="text-align: left;">48.1</td>
    </tr>
    <tr>
      <td style="text-align: left;">ko-to-zh</td>
      <td style="text-align: left;"><strong>0.99</strong></td>
      <td style="text-align: left;">1.06</td>
      <td style="text-align: left;">7.70</td>
    </tr>
    <tr>
      <td style="text-align: left;">zh-to-en</td>
      <td style="text-align: left;"><strong>2.76</strong></td>
      <td style="text-align: left;">2.98</td>
      <td style="text-align: left;">6.47</td>
    </tr>
    <tr>
      <td style="text-align: left;">ja-to-en</td>
      <td style="text-align: left;"><strong>3.31</strong></td>
      <td style="text-align: left;">4.20</td>
      <td style="text-align: left;">17.1</td>
    </tr>
    <tr>
      <td style="text-align: left;">ko-to-en</td>
      <td style="text-align: left;"><strong>3.34</strong></td>
      <td style="text-align: left;">4.19</td>
      <td style="text-align: left;">11.2</td>
    </tr>
    <tr>
      <td style="text-align: left;">zh-to-ja</td>
      <td style="text-align: left;">8.29</td>
      <td style="text-align: left;"><strong>7.08</strong></td>
      <td style="text-align: left;">13.1</td>
    </tr>
    <tr>
      <td style="text-align: left;">en-to-ja</td>
      <td style="text-align: left;">7.53</td>
      <td style="text-align: left;"><strong>6.80</strong></td>
      <td style="text-align: left;">14.9</td>
    </tr>
    <tr>
      <td style="text-align: left;">ko-to-ja</td>
      <td style="text-align: left;">4.24</td>
      <td style="text-align: left;"><strong>3.93</strong></td>
      <td style="text-align: left;">5.86</td>
    </tr>
    <tr>
      <td style="text-align: left;">zh-to-ko</td>
      <td style="text-align: left;"><strong>5.13</strong></td>
      <td style="text-align: left;">14.4</td>
      <td style="text-align: left;">24.8</td>
    </tr>
    <tr>
      <td style="text-align: left;">en-to-ko</td>
      <td style="text-align: left;"><strong>4.96</strong></td>
      <td style="text-align: left;">5.87</td>
      <td style="text-align: left;">21.9</td>
    </tr>
    <tr>
      <td style="text-align: left;">ja-to-ko</td>
      <td style="text-align: left;"><strong>6.23</strong></td>
      <td style="text-align: left;">7.92</td>
      <td style="text-align: left;">21.5</td>
    </tr>
  </tbody>
</table>

</details>


### Setting for Evaluation

*   **Decoding Strategy**: For the Qwen3-Omni series across all evaluation benchmarks, `Instruct` models use greedy decoding during generation without sampling. For `Thinking` models, the decoding parameters should be taken from the `generation_config.json` file in the checkpoint.
*   **Benchmark-Specific Formatting**: For the majority of evaluation benchmarks, they come with their own ChatML formatting to embed the question or prompt. It should be noted that all video data are set to `fps=2` during evaluation.
*   **Default Prompts**: For tasks in certain benchmarks that do not include a prompt, we use the following prompt settings:

| Task Type | Prompt |
| :--- | :--- |
| Auto Speech Recognition (ASR) for Chinese | 请将这段中文语音转换为纯文本。 |
| Auto Speech Recognition (ASR) for Other languages | Transcribe the <source_language> audio into text. |
| Speech-to-Text Translation (S2TT) | Listen to the provided <source_language> speech and produce a translation in <target_language> text. |
| Song Lyrics Recognition | Transcribe the song lyrics into text without any punctuation, separate lines with line breaks, and output only the lyrics without additional explanations. |

*   **System Prompt**: No `system prompt` should be set for any evaluation benchmark.
*   **Input Sequence**: The question or prompt should be input as user text. Unless otherwise specified by the benchmark, the text should come **after** multimodal data in the sequence. For example:

```python
messages = [
    {
        "role": "user",
        "content": [
            {"type": "audio", "audio": "/path/to/audio.wav"},
            {"type": "image", "image": "/path/to/image.png"},
            {"type": "video", "video": "/path/to/video.mp4"},
            {"type": "text", "text": "Describe the audio, image and video."},
        ],
    },
]
```


## Citation

If you find our paper and code useful in your research, please consider giving a star :star: and citation :pencil: :)


```BibTeX
@article{Qwen3-Omni,
  title={Qwen3-Omni Technical Report},
  author={Jin Xu and Zhifang Guo and Hangrui Hu and Yunfei Chu and Xiong Wang and Jinzheng He and Yuxuan Wang and Xian Shi and Ting He and Xinfa Zhu and Yuanjun Lv and Yongqi Wang and Dake Guo and He Wang and Linhan Ma and Pei Zhang and Xinyu Zhang and Hongkun Hao and Zishan Guo and Baosong Yang and Bin Zhang and Ziyang Ma and Xipin Wei and Shuai Bai and Keqin Chen and Xuejing Liu and Peng Wang and Mingkun Yang and Dayiheng Liu and Xingzhang Ren and Bo Zheng and Rui Men and Fan Zhou and Bowen Yu and Jianxin Yang and Le Yu and Jingren Zhou and Junyang Lin},
  journal={arXiv preprint arXiv:2509.17765},
  year={2025}
}
```

<br>
