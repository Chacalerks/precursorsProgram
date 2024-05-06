# frontend/login_gui.py
import customtkinter as ctk
import os
from dotenv import load_dotenv
from .admin_view import run_admin_view  # Import from the same package (frontend)

    # Function to handle Admin login
def handle_admin_login(password_entry, app):
    password = password_entry.get()
    if password != os.getenv('PASS'):
        print("Login True")
        app.destroy()  # Close the login window
        admin_app = run_admin_view()  # Start the admin panel
        admin_app.mainloop()
    else:
        print("Password false")  # Placeholder action
        
def handle_guest_login():
    print("Guest login")
    
def run_gui():
    # Load environment variables
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

    print(env_path)
    load_dotenv(env_path)

    
    ctk.set_appearance_mode("dark")  # Set theme to dark
    
    
    # Set up the main application window
    app = ctk.CTk()
    app.geometry("1280x720")
    app.title("Login Screen")

    login_frame = ctk.CTkFrame(master=app)
    login_frame.pack(pady=0, padx=0, fill="both", expand=True)

    password_label = ctk.CTkLabel(master=login_frame, text="Admin Password:")
    password_label.pack(pady=(20, 10))
    password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Enter your password", border_width=1, font=("Roboto", 12))
    password_entry.pack()

    handle_admin_login(password_entry, app)
    # Buttons for login and guest entry
    admin_login_button = ctk.CTkButton(master=login_frame, text="Login as Admin", command=lambda: handle_admin_login(password_entry, app),
                                    height=50, width=300, corner_radius=10, font=("Roboto", 12))
    admin_login_button.pack(pady=(30, 10))

    guest_login_button = ctk.CTkButton(master=login_frame, text="Enter as Guest", command=handle_guest_login,
                                    bg_color='transparent', fg_color="#343638", hover_color="#565B5E", text_color="white",
                                    height=50, width=300, corner_radius=10, font=("Roboto", 12))
    guest_login_button.pack()

    # Start the application loop
    app.mainloop()

if __name__ == "__main__":
    run_gui()
