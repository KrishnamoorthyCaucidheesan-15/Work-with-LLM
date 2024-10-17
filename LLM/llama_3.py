import boto3
import json

def generate_notes(transcript_file, output_file):
    # Define the long instruction as a variable
    instruction = """
        Your long prompt must be inserted here
    """

     # Initialize the Bedrock client
    client = boto3.client('bedrock-runtime')

    # Read the transcript from the .txt file
    with open(transcript_file, "r") as file:
        transcript = file.read()

    # Combine the instruction and the transcript into the prompt
    prompt = f"{instruction}\n\nTranscript:\n{transcript}"

    payload={
    "prompt":prompt,
    "max_gen_len":1024,
    "temperature":0.2,
    "top_p":1.0
    }


    body=json.dumps(payload)
    model_id="meta.llama3-8b-instruct-v1:0"

    response=client.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
    )

    response_body=json.loads(response.get("body").read())
    response_text=response_body['generation']

    # Write the generated notes to the output file
    with open(output_file, "w") as out_file:
        out_file.write(response_text)
    
    print("Notes generated and written to:", output_file)
   

# Example usage
transcript_file = "path for your transcript file"
output_file = "path for your output file"
generate_notes(transcript_file, output_file)

