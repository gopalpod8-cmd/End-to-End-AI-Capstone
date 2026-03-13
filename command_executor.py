import webbrowser
import os
import pyttsx3
import psutil
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def run_command(command_text):
    query = command_text.lower()
    
    if "search for" in query:
        term = query.replace("search for", "").strip()
        speak(f"Searching for {term}")
        webbrowser.open(f"https://www.google.com/search?q={term}")
        return f"Searching: {term}"

    elif "play" in query:
        song = query.replace("play", "").strip()
        speak(f"Opening YouTube for {song}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        return f"YouTube: {song}"

    elif "battery" in query:
        battery = psutil.sensors_battery()
        speak(f"Battery is at {battery.percent} percent")
        return f"Battery: {battery.percent}%"

    elif "cpu" in query:
        usage = psutil.cpu_percent()
        speak(f"CPU usage is {usage} percent")
        return f"CPU: {usage}%"

    elif "time" in query:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
        return f"Time: {now}"

    elif "open" in query:
        app = query.replace("open ", "").strip()
        if "notepad" in app: os.system("notepad")
        elif "calculator" in app: os.system("calc")
        else: webbrowser.open(f"https://www.google.com/search?q={app}")
        return f"Opening {app}"

    return "Command processed."
