import customtkinter as ctk
from .home_admin_panel import create_home_panel
from .precursors_control_panel import create_precursor_control_panel
from PIL import Image, ImageTk
from frontend.utilitiesFun import resource_path

def switch_event(switch_var):
    print("Switch toggled, current value:", switch_var.get())

def run_admin_view():
    app = ctk.CTk()
    app.geometry("1280x720")
    app.title("Admin Dashboard")

    aside = ctk.CTkFrame(master=app, width=200, corner_radius=0)
    aside.pack(side="left", fill="y")

    content_panel = ctk.CTkFrame(master=app, fg_color="transparent")
    content_panel.pack(side="right", fill="both", expand=True)

    # Switch variable for database control
    switch_var = ctk.StringVar(value="on")
    switchBD = ctk.CTkSwitch(master=aside, text="Habilitar Base de Datos", variable=switch_var,
                                onvalue="on", offvalue="off", command=lambda: switch_event(switch_var))
    switchBD.pack(pady=10, padx=10, side="bottom")

    # Define a function to clear the content panel and add new content
    def switch_panel(panel_function):
        for widget in content_panel.winfo_children():
            widget.destroy()
        panel_function(content_panel, switch_var)  # Pass the switch_var to panel functions

    #-------------------------------------------------------------------------------Aside
    
    # Load image for icons
    logoIcon = resource_path("src/img/GASEL_R_QUIMICA_TRANSPARENTE.png")
    logoIconImage = Image.open(logoIcon)
    
    new_width = 200
    original_width, original_height = logoIconImage.size
    aspect_ratio = original_width / original_height
    new_height = int(new_width / aspect_ratio)
    logoIconPhoto = logoIconImage.resize((new_width, new_height), Image.Resampling.LANCZOS) 
    logoIconPhoto = ImageTk.PhotoImage(logoIconPhoto)
    
    icon = ctk.CTkLabel(master=aside, image=logoIconPhoto, text="")
    icon.image = logoIconPhoto  # Keep a reference!
    icon.pack(pady=(50, 20), padx=20)
    
    # Sidebar buttons
    home_button = ctk.CTkButton(master=aside, text="Home", fg_color="#343638", hover_color="#565B5E", text_color="white",
                                command=lambda: switch_panel(create_home_panel))  # Assuming home panel doesn't need the switch_var
    home_button.pack(pady=10, padx=10, fill="x")

    precurso_control_button = ctk.CTkButton(master=aside, text="Precurso Control", fg_color="#343638", hover_color="#565B5E", text_color="white",
                                            command=lambda: switch_panel(create_precursor_control_panel))
    precurso_control_button.pack(pady=10, padx=10, fill="x")

    # Initialize with the home panel
    switch_panel(create_home_panel)

    return app  # Return the app instance for further manipulation if needed

