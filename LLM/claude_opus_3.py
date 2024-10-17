import anthropic

# Initialize the Claude client using your API key
client = anthropic.Client(api_key="insert your api key here")

def generate_notes_claude(transcript_file, output_file):
    # Define the long instruction as a variable
    instruction = """
    Your long prompt must be inserted here
    """

    # Read the transcript from the .txt file
    with open(transcript_file, "r") as file:
        transcript = file.read()

    # Construct the complete prompt
    full_prompt = f"{instruction}\n\nHuman:\n{transcript}\n\nAssistant:"
    completion = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": full_prompt}
        ]
    )

    # Get the notes content
    notes = completion.content

    # Convert notes to string if it is not already
    if isinstance(notes, str):
        notes_str = notes
    else:
        notes_str = str(notes)  

    # Save the notes in a .txt file
    with open(output_file, "w") as file:
        file.write(notes_str)


# Example usage
transcript_file = "path for your transcript file"
output_file = "path for your output file"
generate_notes_claude(transcript_file, output_file)
