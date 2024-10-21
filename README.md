# Work with LLM

## Project: AI Transcription & LLM Integration

This repository demonstrates how to integrate the out put of transcription services with various Large Language Models (LLMs), showcasing the use of OpenAI’s GPT-4, Claude, LLaMA, and more. The files in this repository explain the end-to-end process, from transcription of audio inputs using OpenAI’s Whisper model to generating responses from LLMs via API keys and AWS Bedrock.

### File Overview

1. transcription.py

This file details the transcription process using OpenAI's Whisper model, a state-of-the-art automatic speech recognition (ASR) model. It provides an implementation for transcribing audio files into text, which can then be used as input for LLMs.

Model: Whisper (OpenAI)

Usage: Converts audio into text.

Purpose: Generates the transcription that will be sent as a prompt to LLMs for further processing.

2. claude_haiku_3.py

This file connects the transcription output to the Claude 3 Haiku model, which is accessed via an API key. It demonstrates how to send the text transcription to Claude and receive a response based on the prompt.

Model: Claude 3 Haiku (Anthropic)

Access: API Key

Purpose: Utilizes Claude’s LLM capabilities to process the transcription and provide meaningful responses or insights.

3. claude_opus_3.py

Similar to claude_haiku_3.py, this file integrates the Claude 3 Opus model. It shows how to link the transcription data to another variant of the Claude model, offering flexibility in generating responses based on different versions of the LLM.

Model: Claude 3 Opus (Anthropic)

Access: API Key

Purpose: Handles the transcription prompt and generates comprehensive output with Claude 3 Opus.

4. claude_sonnet_3.5.py

This file connects the transcription to the Claude 3.5 Sonnet model, illustrating the use of the Claude model for generating more complex or creative outputs. This integration uses an API key to connect the transcription to the Claude model.

Model: Claude 3.5 Sonnet (Anthropic)

Access: API Key

Purpose: Processes transcription input through Claude 3.5 Sonnet for advanced or creative tasks.

5. gpt_4.py

This file demonstrates how to integrate transcription output with OpenAI's GPT-4 model. Using the OpenAI API key, it sends the transcription as a prompt to GPT-4, generating detailed and context-aware responses.

Model: GPT-4 (OpenAI)

Access: API Key

Purpose: Converts transcription into intelligent, context-based responses using GPT-4's powerful natural language understanding.

6. llama_3.py

This file explains how to connect transcription outputs to the LLaMA 3 model using AWS Bedrock. It demonstrates how to interface with LLaMA through AWS Bedrock’s services to generate LLM-based responses.

Model: LLaMA 3 (Meta)

Access: AWS Bedrock

Purpose: Uses LLaMA 3 on AWS Bedrock to interpret transcription data and provide efficient, scalable AI responses.

7. token_counter.py

This is a utility file that counts the tokens in a given prompt before sending it to the LLM. Tokenization is a crucial step in interacting with LLMs, as models like GPT-4 and Claude have token limits, and exceeding these limits can result in incomplete or truncated responses.

Purpose: Ensures the prompt is within token limits for API calls, avoiding errors or incomplete responses.

Importance: Proper token management is essential when working with LLMs to maximize performance and ensure cost-effective use of API services.

## LLM Access Breakdown

### LLMs accessed via API Key:

Claude 3 Haiku  
Claude 3 Opus  
Claude 3.5 Sonnet  
GPT-4    
These models are accessed through their respective API keys, providing flexibility for integrating them into any cloud-based or on-premise solution that requires an API interface.

### LLMs accessed via AWS Bedrock:

#### LLaMA 3

LLaMA 3 is connected through AWS Bedrock, offering a scalable, managed environment where the model can be deployed for robust AI-driven applications.

#### Importance of token_counter.py

Tokenization is a key process when working with LLMs. LLMs operate on tokens, which are chunks of text (e.g., words or parts of words). LLM APIs, including OpenAI and Claude, have specific token limits for input prompts and responses. The token_counter.py file ensures that your prompts adhere to these limits, preventing issues like truncated outputs or API errors. By using this file, you can optimize your prompts for maximum efficiency and cost management.

#### Conclusion

This repository provides an end-to-end solution for transcription and LLM integration. From using OpenAI Whisper for transcription to connecting with LLMs like Claude, GPT-4, and LLaMA via API keys and AWS Bedrock, it offers versatile ways to generate responses from text data. The token counter ensures smooth interactions with these models, helping manage prompt sizes and preventing errors.
