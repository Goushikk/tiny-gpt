import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Define a function to send a message to ChatGPT
def send_message(message):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the model
        prompt=message,
        max_tokens=50,  # Adjust the response length as needed
        n=1,  # Generate a single response
        stop=None,  # Stop early if needed
        temperature=0.7  # Control the randomness of the response
    )
    return response.choices[0].text.strip()

# Example usage
while True:
    user_input = input("User: ")
    if user_input.lower() == 'bye':
        print("ChatGPT: Goodbye!")
        break
    response = send_message(user_input)
    print("ChatGPT:", response)
