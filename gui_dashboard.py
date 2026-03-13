import customtkinter as ctk
import vision_engine
import command_executor
import threading

# Set the look and feel
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AICapstoneGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Capstone Control Center")
        self.geometry("600x450")

        # --- UI LAYOUT ---
        self.label = ctk.CTkLabel(self, text="AI SECURITY SYSTEM", font=("Roboto", 24, "bold"))
        self.label.pack(pady=20)

        self.status_frame = ctk.CTkFrame(self)
        self.status_frame.pack(pady=10, padx=20, fill="x")

        self.status_light = ctk.CTkLabel(self.status_frame, text="● SYSTEM STANDBY", text_color="yellow")
        self.status_light.pack(pady=10)

        self.auth_button = ctk.CTkButton(self, text="START AUTHENTICATION", command=self.start_auth_thread)
        self.auth_button.pack(pady=20)

        self.log_box = ctk.CTkTextbox(self, width=500, height=150)
        self.log_box.pack(pady=10)
        self.log_box.insert("0.0", "System ready. Click button to begin...\n")

    def log(self, text):
        self.log_box.insert("end", f"> {text}\n")
        self.log_box.see("end")

    def start_auth_thread(self):
        # We run AI in a separate thread so the GUI doesn't freeze
        self.auth_button.configure(state="disabled")
        threading.Thread(target=self.run_ai_logic, daemon=True).start()

    def run_ai_logic(self):
        self.status_light.configure(text="● SCANNING FACE...", text_color="orange")
        self.log("Initializing Vision Engine...")
        
        if vision_engine.authenticate_user():
            self.status_light.configure(text="● ACCESS GRANTED", text_color="green")
            self.log("Identity Verified: Welcome Gopal.")
            
            # Ask for command via a simple dialog
            dialog = ctk.CTkInputDialog(text="Enter your command:", title="AI Command")
            cmd = dialog.get_input()
            
            if cmd:
                self.log(f"Processing command: {cmd}")
                result = command_executor.run_command(cmd)
                self.log(result)
        else:
            self.status_light.configure(text="● ACCESS DENIED", text_color="red")
            self.log("Authentication Failed. Security log created.")
            
        self.auth_button.configure(state="normal")

if __name__ == "__main__":
    app = AICapstoneGUI()
    app.mainloop()