import time
import sys
import random
from datetime import datetime
from zoneinfo import ZoneInfo

def typing_effect(text, speed=0.02):
    """Prints text to the screen with a clean typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def get_response(user_input):
    user_input = user_input.strip().lower()
    
    # Precise dictionary routing mapping standard input keywords to specific responses
    responses = {
        ("hello", "hi", "hey", "yo"): "👋 Hi there! Super glad you dropped by. How can I help you today?",
        ("how are you", "how's it going", "sup"): "⚡ I'm running at 100% efficiency! Thanks for checking in.",
        ("what is your name", "who are you", "identity"): "🤖 I am the CodeAlpha Advanced Rule-Based Chatbot, built entirely in Python!",
        ("help", "commands", "what can you do"): "📋 You can chat with me naturally, ask me for a 'joke', ask for 'time', ask for 'date', or type 'bye' to exit!",
        ("bye", "goodbye", "exit", "quit"): "🚀 Mission complete. Goodbye! Have an absolutely spectacular day!"
    }
    
    # 1. Check exact dictionary rules
    for keywords, reply in responses.items():
        if user_input in keywords:
            return reply
            
    # 2. Dynamic single joke selector
    if user_input in ["joke", "tell me a joke", "make me laugh"]:
        joke_pool = [
            "Why do programmers wear glasses? Because they can't C#!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
            "There are 10 types of people in the world: those who understand binary, and those who don't.",
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "['hip', 'hip'] - (hip hip array!)",
            "To understand what recursion is, you must first understand what recursion is.",
            "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",
            "Why do Java programmers have to wear glasses? Because they don't C#.",
            "What is a programmer's favorite hangout place? The Foo Bar.",
            "Real programmers count from 0."
        ]
        return f"🃏 {random.choice(joke_pool)}"
        
    # 3. Dynamic Local Clock Logic
    elif user_input in ["time", "clock"]:
        local_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        return f"⏰ System time check: The current local time is {local_time.strftime('%I:%M:%S %p')}."
        
    # 4. Dynamic Local Calendar Logic
    elif user_input in ["date", "calendar"]:
        local_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        return f"📅 System date check: Today's date is {local_time.strftime('%d-%m-%Y')}."
        
    # 5. Fallback Response
    return "🤔 Hmm, I don't quite have a rule for that string yet. Type 'help' to see what I can do!"

def main():
    print("==================================================")
    print("🤖  WELCOME TO THE UPGRADED CODEALPHA CHATBOT  🤖")
    print("==================================================")
    typing_effect("Initializing system protocols...\nConnecting to core terminal interface...\nReady for input!\n", speed=0.01)
    print("💡 Tip: Type 'help' to see available features or 'bye' to quit.\n")
    
    while True:
        user_input = input("👤 You ➜ ")
        if not user_input.strip():
            continue
            
        response = get_response(user_input)
        
        # Smooth processing buffer effect
        sys.stdout.write("🤖 Bot is typing...")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\r" + " " * 20 + "\r")
        sys.stdout.flush()
        
        # Display response text cleanly
        sys.stdout.write("🤖 Bot ➜ ")
        typing_effect(response, speed=0.015)
        print() 
        
        # Terminate gracefully when exit command is validated
        if user_input.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    main()
