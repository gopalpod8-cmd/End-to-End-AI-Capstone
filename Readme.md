# 🛡️ AI-Powered Biometric Security Dashboard
### *End-to-End AI Capstone Project*

A modern, modular Python application that replaces traditional passwords with **Biometric Identity Verification**. This system "sees" the user, authenticates their identity using 128-point facial encoding, and provides a voice-enabled dashboard for system automation.



---

## 🚀 Key Features

* **Real-Time Biometrics:** Uses HOG (Histogram of Oriented Gradients) and Deep Learning to verify identity via webcam.
* **Intruder Alert System:** Automatically detects unauthorized users, issues a vocal warning, and captures a timestamped "mugshot" in the `/intruders` folder.
* **Voice-Enabled Automation:** Integrated **pyttsx3** for offline Text-to-Speech (TTS) feedback—no internet required for the AI to talk.
* **Modern GUI Dashboard:** A sleek, dark-mode interface built with **CustomTkinter** that uses **Multithreading** to keep the UI responsive during AI processing.
* **Modular Design:** Clean separation of concerns between Vision, Logic, and UI modules for professional-grade maintainability.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI/Vision:** OpenCV, Dlib, Face_Recognition
* **GUI:** CustomTkinter
* **Audio:** Pyttsx3 (Offline TTS)
* **OS Interaction:** Webbrowser, OS, Subprocess

---

## 📂 Project Structure

```text
End-to-End AI Capstone/
├── gui_dashboard.py       # Main Application Entry Point
├── vision_engine.py       # AI Face Recognition Logic
├── command_executor.py    # Automation & Voice Rules
├── authorized_users/      # Store your 'me.jpeg' here
├── intruders/             # Automatic logs of failed attempts
├── requirements.txt       # List of dependencies
└── README.md              # Project Documentation
