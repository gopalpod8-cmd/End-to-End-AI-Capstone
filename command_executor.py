import webbrowser
import os
import pyttsx3
from datetime import datetime

# Initialize the Voice Engine
engine = pyttsx3.init()

# Optional: Adjust the voice properties
engine.setProperty('rate', 170)    # Speed (150-200 is natural)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

def speak(text):
    """Utility function to make the AI speak."""
    print(f"AI: {text}") # Still print to console for debugging
    engine.say(text)
    engine.runAndWait()

def run_command(command_text):
    """
    The Command Executor 'Brain'. 
    Maps user input to system actions.
    """
    command_text = command_text.lower()
    
    # 1. WEB AUTOMATION
    if "google" in command_text:
        speak("Opening Google Chrome.")
        webbrowser.open("https://www.google.com")
        return "Action Complete: Browser Opened."

    elif "linkedin" in command_text:
        speak("Opening your LinkedIn profile. Good luck with the networking!")
        webbrowser.open("https://www.linkedin.com/in/your-profile-link") # Replace with your link
        return "Action Complete: LinkedIn Opened."

    elif "github" in command_text:
        speak("Accessing your GitHub repositories.")
        webbrowser.open("https://github.com/") # Replace with your link
        return "Action Complete: GitHub Opened."

    # 2. SYSTEM UTILITIES
    elif "time" in command_text:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}.")
        return f"Reported Time: {now}"

    elif "calculator" in command_text:
        speak("Launching the system calculator.")
        os.system("calc")
        return "Action Complete: Calculator Launched."

    elif "notepad" in command_text:
        speak("Opening Notepad for your notes.")
        os.system("notepad")
        return "Action Complete: Notepad Launched."

    # 3. EXIT COMMAND
    elif "shutdown" in command_text or "exit" in command_text:
        speak("System shutting down. Goodbye Gopal.")
        return "EXIT"

    # 4. FALLBACK
    else:
        speak("Command received, but I don't have a specific rule for that action yet.")
        return "Unknown Command."

if __name__ == "__main__":
    # Test block to run this module independently
    print("Testing Command Executor (Voice Enabled)...")
    test_cmd = input("Enter test command: ")
    run_command(test_cmd)