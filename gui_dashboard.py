import customtkinter as ctk
import vision_engine
import command_executor
import threading

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AIApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI Capstone v2.0")
        self.geometry("600x550")

        self.label = ctk.CTkLabel(self, text="AI SECURITY SYSTEM", font=("Roboto", 24, "bold"))
        self.label.pack(pady=20)

        self.status_box = ctk.CTkFrame(self)
        self.status_box.pack(pady=10, fill="x", padx=40)
        self.status_label = ctk.CTkLabel(self.status_box, text="● SYSTEM STANDBY", text_color="yellow")
        self.status_label.pack(pady=10)

        # BUTTON 1: Authenticate
        self.btn_auth = ctk.CTkButton(self, text="START AUTHENTICATION", command=self.auth_thread)
        self.btn_auth.pack(pady=15)

        # BUTTON 2: Enroll (The missing one!)
        self.btn_reg = ctk.CTkButton(self, text="ENROLL NEW USER", fg_color="transparent", border_width=1, command=self.reg_thread)
        self.btn_reg.pack(pady=10)

        self.logs = ctk.CTkTextbox(self, width=500, height=200)
        self.logs.pack(pady=20)
        self.log_msg("System ready. Enroll a user or start authentication.")

    def log_msg(self, msg):
        self.logs.insert("end", f"> {msg}\n")
        self.logs.see("end")

    def auth_thread(self):
        threading.Thread(target=self.do_auth, daemon=True).start()

    def reg_thread(self):
        threading.Thread(target=self.do_reg, daemon=True).start()

    def do_reg(self):
        self.status_label.configure(text="● CAPTURING FACE...", text_color="blue")
        if vision_engine.register_new_user():
            self.status_label.configure(text="● USER ENROLLED", text_color="green")
            self.log_msg("Success: Face captured and saved.")
        else:
            self.log_msg("Failed to capture face.")

    def do_auth(self):
        self.status_label.configure(text="● SCANNING...", text_color="orange")
        if vision_engine.authenticate_user():
            self.status_label.configure(text="● ACCESS GRANTED", text_color="green")
            dialog = ctk.CTkInputDialog(text="Enter Command:", title="Authorized")
            cmd = dialog.get_input()
            if cmd:
                res = command_executor.run_command(cmd)
                self.log_msg(res)
        else:
            self.status_label.configure(text="● ACCESS DENIED", text_color="red")
            self.log_msg("Intruder detected!")

if __name__ == "__main__":
    app = AIApp()
    app.mainloop()
