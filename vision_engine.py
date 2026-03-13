import face_recognition
import cv2
import os
import glob
import pyttsx3
from datetime import datetime

# Initialize Voice Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150) # Speed of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def authenticate_user():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_dir, "authorized_users")
    
    possible_files = glob.glob(os.path.join(folder_path, "me*"))
    if not possible_files:
        print("[ERROR] No 'me' photo found.")
        return False

    image_path = possible_files[0]

    try:
        me_image = face_recognition.load_image_file(image_path)
        me_encoding = face_recognition.face_encodings(me_image)[0]
    except Exception as e:
        print(f"[ERROR] AI Loading Error: {e}")
        return False

    video_capture = cv2.VideoCapture(0)
    speak("System active. Identifying user.")

    authenticated = False
    last_frame = None

    for _ in range(60):
        ret, frame = video_capture.read()
        if not ret: break
        last_frame = frame # Save for security capture

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces([me_encoding], face_encoding, tolerance=0.6)
            if True in matches:
                authenticated = True
                break
        if authenticated: break

    # --- SECURITY FEATURE: INTRUDER ALERT ---
    if authenticated:
        speak("Access granted. Welcome back Gopal.")
    else:
        speak("Access denied. Intruder detected.")
        # Create folder if it doesn't exist
        intruder_folder = os.path.join(base_dir, "intruders")
        if not os.path.exists(intruder_folder):
            os.makedirs(intruder_folder)
        
        # Save photo of the intruder
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        cv2.imwrite(f"{intruder_folder}/intruder_{timestamp}.jpg", last_frame)
        print(f"⚠️ SECURITY: Intruder photo saved to {intruder_folder}")

    video_capture.release()
    cv2.destroyAllWindows()
    return authenticated