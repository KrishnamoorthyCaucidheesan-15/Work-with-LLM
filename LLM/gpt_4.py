from openai import OpenAI
client = OpenAI(api_key="insert your api key here")

def generate_notes(transcript_file, output_file):
    # Define the long instruction as a variable
    instruction = """
        Your long prompt must be inserted here
    """

    # Read the transcript from the .txt file
    with open(transcript_file, "r") as file:
        transcript = file.read()

    # Combine instruction and transcript into one continuous prompt
    full_prompt = f"{instruction}\n{transcript}"
    print(full_prompt)

    # Create notes using the GPT model
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": full_prompt}
        ]
    )

    # Get the notes content
    notes = completion.choices[0].message.content

    # Save the notes in a .txt file
    with open(output_file, "w") as file:
        file.write(notes)

# Example usage
transcript_file = "path for your transcript file"
output_file = "path for your output file"
generate_notes(transcript_file, output_file)
