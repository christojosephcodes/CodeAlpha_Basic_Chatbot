def get_response(user_input):
    # Convert input to lowercase to handle mixed case variations smoothly
    user_input = user_input.strip().lower()
    
    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"
    elif user_input in ["how are you", "how's it going"]:
        return "I'm fine, thanks! How are you doing?"
    elif user_input in ["what is your name", "who are you"]:
        return "I am a simple rule-based Python chatbot."
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't quite understand that. Could you try saying 'hello', 'how are you', or 'bye'?"

def main():
    print("==========================================")
    print("🤖 Welcome to the CodeAlpha Rule-Based Chatbot!")
    print("Type 'bye' to exit the conversation.")
    print("==========================================\n")
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}\n")
        
        if user_input.strip().lower() in ["bye", "goodbye", "exit"]:
            break

if __name__ == "__main__":
    main()
