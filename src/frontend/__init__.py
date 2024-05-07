# frontend/login_gui.py
import customtkinter as ctk
import os
from .admin_view import run_admin_view  # Import from the same package (frontend)
from frontend.utilitiesFun import load_environment_vars, resource_path, resize_image


# ---------------------------------------------------------------
# Event Handlers
# ---------------------------------------------------------------

def handle_admin_login(password_entry, app):
    """Function to handle Admin login."""
    password = password_entry.get()
    if password != os.getenv('PASS'):
        print("Login True")
        app.destroy()  # Close the login window
        admin_app = run_admin_view()  # Start the admin panel
        admin_app.mainloop()
    else:
        print("Password false")

def handle_guest_login():
    """Function to handle Guest login."""
    print("Guest login")

# ---------------------------------------------------------------
# GUI Setup
# ---------------------------------------------------------------

def setup_gui():
    """Set up the main application window and components."""
    app = ctk.CTk()
    app.geometry("1280x720")
    app.title("Login Screen")
    return app

def setup_login_frame(app):
    """Set up the login frame and its components."""
    login_frame = ctk.CTkFrame(master=app)
    login_frame.pack(pady=(100, 100), padx=(300, 300), fill="both", expand=True)
    return login_frame

def add_login_elements(login_frame):
    """Add elements like labels, entries, and buttons to the login frame."""
    # Load and display logo
    logo_path = resource_path("src/img/GASEL_R_QUIMICA_TRANSPARENTE.png")
    logo_photo = resize_image(logo_path, 300)
    icon = ctk.CTkLabel(master=login_frame, image=logo_photo, text="")
    icon.image = logo_photo  # Keep a reference!
    icon.pack(pady=(50, 0), padx=10)

    # Add labels
    title_label = ctk.CTkLabel(master=login_frame, text="Sistema de Control de Precursores:" , font=("Roboto", 22, "bold"))
    title_label.pack(pady=(20, 5))
    subtitle_label = ctk.CTkLabel(master=login_frame, text="¡Bienvenido! Ingrese su información:" , font=("Roboto Light", 12))
    subtitle_label.pack(pady=(0, 10))

    # Add password entry
    password_label = ctk.CTkLabel(master=login_frame, text="Contraseña:" , font=("Roboto", 16, "bold"))
    password_label.pack(pady=(10, 10))
    password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Enter your password", width=300, border_width=1, show="*", font=("Roboto", 12))
    password_entry.pack()

    return password_entry

def add_buttons(login_frame, password_entry, app):
    """Add buttons for admin and guest login."""
    admin_login_button = ctk.CTkButton(master=login_frame, text="Login as Admin", command=lambda: handle_admin_login(password_entry, app),
                                    height=40, width=300, corner_radius=10, font=("Roboto", 12))
    admin_login_button.pack(pady=(50, 20))
    guest_login_button = ctk.CTkButton(master=login_frame, text="Enter as Guest", command=handle_guest_login,
                                    bg_color='transparent', fg_color="#343638", hover_color="#565B5E", text_color="white",
                                    height=40, width=300, corner_radius=10, font=("Roboto", 12))
    guest_login_button.pack()

def run_gui():
    """Initialize the GUI and start the application loop."""
    load_environment_vars()
    ctk.set_appearance_mode("dark")  # Set theme to dark
    app = setup_gui()
    login_frame = setup_login_frame(app)
    password_entry = add_login_elements(login_frame)
    add_buttons(login_frame, password_entry, app)
    app.mainloop()

if __name__ == "__main__":
    run_gui()
