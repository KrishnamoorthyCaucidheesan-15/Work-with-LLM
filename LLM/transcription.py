from openai import OpenAI
client = OpenAI(api_key="insert your api key here")

# your audio file path should be attached here
audio_file_location = "test.m4a"
# location to save your transcript file
transcription_file = "transcript.txt"

def whisper_transcription(audio_file_location):
    with open(audio_file_location, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            temperature="0.6",
            response_format="text"
        )
    return transcription

# Get the transcript
transcript = whisper_transcription(audio_file_location)

# Save the transcript to a text file
with open(transcription_file, "w") as file:
    file.write(transcript)

print(f"Transcription saved to {transcription_file}")
