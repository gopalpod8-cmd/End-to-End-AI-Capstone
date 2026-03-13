import webbrowser
import os
import pyttsx3
import psutil # You might need to: pip install psutil
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

def run_command(command_text):
    query = command_text.lower()
    
    # --- 1. DYNAMIC WEB SEARCH ---
    if "search for" in query:
        search_term = query.replace("search for", "").strip()
        speak(f"Searching Google for {search_term}")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
        return f"Searched for: {search_term}"

    elif "play" in query:
        song = query.replace("play", "").strip()
        speak(f"Opening YouTube to play {song}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        return f"Playing: {song} on YouTube"

    # --- 2. SYSTEM STATUS (Intelligence) ---
    elif "battery" in query:
        battery = psutil.sensors_battery()
        percent = battery.percent
        speak(f"The system battery is at {percent} percent.")
        return f"Battery: {percent}%"

    elif "cpu" in query:
        usage = psutil.cpu_percent()
        speak(f"Current CPU usage is at {usage} percent.")
        return f"CPU Usage: {usage}%"

    # --- 3. DYNAMIC APP OPENING ---
    elif "open" in query:
        app_name = query.replace("open", "").strip()
        
        if "chrome" in app_name:
            os.startfile("chrome.exe") # Assumes Chrome is in PATH
            speak("Opening Chrome")
        elif "code" in app_name or "vs code" in app_name:
            os.system("code")
            speak("Opening Visual Studio Code")
        else:
            # Fallback to search if it's not a known app
            speak(f"I don't have a shortcut for {app_name}, opening it in Google.")
            webbrowser.open(f"https://www.google.com/search?q={app_name}")
        return f"Tried to open {app_name}"

    # --- 4. DEFAULT COMMANDS ---
    elif "time" in query:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"It is currently {now}")
        return f"Time: {now}"

    else:
        speak("Command processed, but no specific action mapped.")
        return "Action: Generic Process"
