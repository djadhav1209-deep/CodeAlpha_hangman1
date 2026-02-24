# Simple Rule-Based Chatbot

def chatbot_reply(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for matching
    if user_input == "hello":
        return "Hi!👋"
    elif user_input == "how are you":
        return "I'm fine, thanks!🙂"
    elif user_input == "bye":
        return "Goodbye!👋"
    else:
        return "Sorry, I don't understand.🤔"

print("💬 Chatbot: Hello! You can say 'hello', 'how are you', or 'bye'.")

while True:
    user_message = input("You: ")
    response = chatbot_reply(user_message)
    print("Chatbot:", response)
    
    if user_message.lower() == "bye":
        break
