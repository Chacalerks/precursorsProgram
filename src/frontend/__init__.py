# frontend/login_gui.py
import customtkinter as ctk
import os
from dotenv import load_dotenv
from .admin_view import run_admin_view  # Import from the same package (frontend)
from PIL import Image, ImageTk
from frontend.utilitiesFun import resource_path, getLabs

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
    login_frame.pack(pady=(100,100), padx=(300,300), fill="both", expand=True)
    
    # Load image for icons
    logoIcon = resource_path("src/img/GASEL_R_QUIMICA_TRANSPARENTE.png")
    logoIconImage = Image.open(logoIcon)
    
    new_width = 300
    original_width, original_height = logoIconImage.size
    aspect_ratio = original_width / original_height
    new_height = int(new_width / aspect_ratio)
    logoIconPhoto = logoIconImage.resize((new_width, new_height), Image.Resampling.LANCZOS) 
    logoIconPhoto = ImageTk.PhotoImage(logoIconPhoto)
    
    icon = ctk.CTkLabel(master=login_frame, image=logoIconPhoto, text="")
    icon.image = logoIconPhoto  # Keep a reference!
    icon.pack(pady=(50, 0), padx=10)

    title_label = ctk.CTkLabel(master=login_frame, text="Sistema de Control de Precursores:" , font=("Roboto", 22, "bold"))
    title_label.pack(pady=(20, 5))
    
    title_label = ctk.CTkLabel(master=login_frame, text="¡Bienvenido! Ingrese su información:" , font=("Roboto Light", 12))
    title_label.pack(pady=(0, 10))
    
    password_label = ctk.CTkLabel(master=login_frame, text="Contraseña:" , font=("Roboto", 16, "bold"))
    password_label.pack(pady=(10, 10))
    password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Enter your password", width=300, border_width=1,show="*", font=("Roboto", 12))
    password_entry.pack()

    handle_admin_login(password_entry, app)
    # Buttons for login and guest entry
    admin_login_button = ctk.CTkButton(master=login_frame, text="Login as Admin", command=lambda: handle_admin_login(password_entry, app),
                                    height=40, width=300, corner_radius=10, font=("Roboto", 12))
    admin_login_button.pack(pady=(50, 20))

    guest_login_button = ctk.CTkButton(master=login_frame, text="Enter as Guest", command=handle_guest_login,
                                    bg_color='transparent', fg_color="#343638", hover_color="#565B5E", text_color="white",
                                    height=40, width=300, corner_radius=10, font=("Roboto", 12))
    guest_login_button.pack()

    # Start the application loop
    app.mainloop()

if __name__ == "__main__":
    run_gui()
