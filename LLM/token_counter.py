import tiktoken

# Define the output text
output_text = '''
    Your long prompt must be inserted here
'''
# Get the encoding for the model
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Encode the output text and calculate the number of tokens
tokens = encoding.encode(output_text)
num_tokens = len(tokens)
print(f"Number of tokens: {num_tokens}")
