# ⚙️ Technical System Design

This document explains the internal workflow and logic of the AI Security Capstone.

## 🔄 The Logic Flow
1. **START:** User launches `gui_dashboard.py`.
2. **AUTH:** User clicks "Start Authentication" -> `vision_engine.py` is called in a separate thread.
3. **SCAN:** Webcam activates -> Face detected -> Comparison made against `me.jpeg`.
4. **DECIDE:**
   - **MATCH:** `Speak("Access Granted")` -> Open Command Input.
   - **NO MATCH:** `Speak("Intruder Detected")` -> Save photo to `/intruders`.
5. **ACT:** User enters command -> `command_executor.py` triggers OS-level action.

## 🛠️ Threading Model
To prevent the GUI from freezing during heavy AI computation, the **Vision Engine** runs on a background `daemon thread`. This allows the "Scanning" animation to stay smooth on the main UI thread.

## 📐 AI Methodology
- **Face Detection:** HOG (Histogram of Oriented Gradients)
- **Face Recognition:** Deep Metric Learning (128D Embeddings)
- **Voice:** SAPI5 (Windows native TTS) via pyttsx3
