import vision_engine
import command_executor

def start_capstone():
    print("--- END-TO-END AI CAPSTONE INITIALIZED ---")
    
    # Step 1: Authenticate
    if vision_engine.authenticate_user():
        print("✅ ACCESS GRANTED: User Identified.")
        
        # Step 2: Accept Command
        command = input("Please enter a command: ")
        
        # Step 3: Execute
        result = command_executor.run_command(command)
        print(f"SYSTEM: {result}")
        
    else:
        print("❌ ACCESS DENIED: Face not recognized.")

if __name__ == "__main__":
    start_capstone()