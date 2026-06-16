import time
import sys
import random

def typing_effect(text, speed=0.02):
    """Prints text to the screen with a vintage terminal typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def get_response(user_input):
    user_input = user_input.strip().lower()
    
    # Simple joke repository
    jokes = [
        "Why do programmers wear glasses? Because they can't C#!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "There are 10 types of people in the world: those who understand binary, and those who don't."
    ]
    
    if user_input in ["hello", "hi", "hey", "yo"]:
        return "👋 Hi there! Super glad you dropped by. How can I help you today?"
    elif user_input in ["how are you", "how's it going", "sup"]:
        return "⚡ I'm running at 100% efficiency! Thanks for checking in. How are things on your end?"
    elif user_input in ["what is your name", "who are you", "identity"]:
        return "🤖 I am the CodeAlpha Advanced Rule-Based Chatbot, built entirely in Python!"
    elif user_input in ["help", "commands", "what can you do"]:
        return "📋 You can chat with me naturally, ask me for a 'joke', ask for the 'time', or type 'bye' to exit!"
    elif user_input in ["joke", "tell me a joke", "make me laugh"]:
        return f"🃏 {random.choice(jokes)}"
    elif user_input in ["time", "date", "clock"]:
        current_time = time.strftime("%H:%M:%S")
        return f"⏰ System time check: The current time is {current_time}."
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "🚀 Mission complete. Goodbye! Have an absolutely spectacular day!"
    else:
        return "🤔 Hmm, I don't quite have a rule for that string yet. Type 'help' to see what I can do!"

def main():
    print("==================================================")
    print("🤖  WELCOME TO THE UPGRADED CODEALPHA CHATBOT  🤖")
    print("==================================================")
    typing_effect("Initializing system protocols...\nConnecting to core terminal interface...\nReady for input!\n", speed=0.01)
    print("💡 Tip: Type 'help' to see available features or 'bye' to quit.\n")
    
    while True:
        # Use a clean prompt arrow for user input
        user_input = input("👤 You ➜ ")
        
        # Get response logic
        response = get_response(user_input)
        
        # Add a realistic processing pause effect
        sys.stdout.write("🤖 Bot is typing...")
        sys.stdout.flush()
        time.sleep(0.6)
        # Erase the "Bot is typing..." line cleanly
        sys.stdout.write("\r" + " " * 20 + "\r")
        sys.stdout.flush()
        
        # Print with the dynamic text delay effect
        sys.stdout.write("🤖 Bot ➜ ")
        typing_effect(response, speed=0.02)
        print() # Extra spacing for scannability
        
        # Smoothly break the execution loop if exit keyword detected
        if user_input.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    main()
