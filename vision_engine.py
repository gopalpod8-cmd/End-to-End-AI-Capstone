import face_recognition
import cv2
import os
import glob
import pyttsx3
from datetime import datetime

# Initialize Voice
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def register_new_user():
    """Captures a frame and saves it as the authorized identity."""
    cap = cv2.VideoCapture(0)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "authorized_users", "me.jpeg")
    
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))

    for _ in range(30): # Let camera adjust
        cap.read()
    
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(save_path, frame)
        cap.release()
        return True
    cap.release()
    return False

def authenticate_user():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_dir, "authorized_users")
    
    possible_files = glob.glob(os.path.join(folder_path, "me*"))
    if not possible_files:
        speak("No registered user found. Please enroll first.")
        return False

    image_path = possible_files[0]
    
    try:
        me_image = face_recognition.load_image_file(image_path)
        me_encoding = face_recognition.face_encodings(me_image)[0]
    except Exception as e:
        print(f"Error: {e}")
        return False

    cap = cv2.VideoCapture(0)
    speak("Camera active. Verifying identity.")

    authenticated = False
    last_frame = None

    for _ in range(60): 
        ret, frame = cap.read()
        if not ret: break
        last_frame = frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces([me_encoding], face_encoding, tolerance=0.6)
            if True in matches:
                authenticated = True
                break
        if authenticated: break

    cap.release()
    cv2.destroyAllWindows()

    if authenticated:
        speak("Access granted. Welcome back.")
    else:
        speak("Access denied. Intruder alert.")
        intruder_dir = os.path.join(base_dir, "intruders")
        if not os.path.exists(intruder_dir): os.makedirs(intruder_dir)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        cv2.imwrite(os.path.join(intruder_dir, f"intruder_{timestamp}.jpg"), last_frame)
        
    return authenticated
    
