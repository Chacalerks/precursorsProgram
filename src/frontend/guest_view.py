# admin_view.py
import customtkinter as ctk
#from .home_admin_panel import create_home_panel
from .precursors_control_panel import create_precursor_control_panel
from PIL import Image, ImageTk
from frontend.utilitiesFun import resource_path, resize_image

from functions import check_labs_report_on_month, load_collection, create_monthly_report, writeSummedSubstances, check_month_report

# ---------------------------------------------------------------
# Initialization
# ---------------------------------------------------------------
load_collection()  

def create_home_panel(parent, _):
    """Create the main home panel with reports and data."""
    title_label = ctk.CTkLabel(master=parent, text="Building Home Panel", font=("Roboto", 24), anchor="w")
    title_label.pack(pady=(40, 20), padx=20, fill="x")

    cards_container = ctk.CTkFrame(master=parent, fg_color="transparent")
    cards_container.pack(pady=5, padx=20, fill="x", expand=True)


# ---------------------------------------------------------------
# Event Handlers
# ---------------------------------------------------------------

def switch_event(switch_var):
    """Handle switch toggle event."""
    print("Switch toggled, current value:", switch_var.get())

# ---------------------------------------------------------------
# Utility Functions
# ---------------------------------------------------------------

def setup_sidebar(app):
    """Setup the sidebar frame with logo and navigation buttons."""
    aside = ctk.CTkFrame(master=app, width=200, corner_radius=0)
    aside.pack(side="left", fill="y")

    # Load and display logo
    logo_path = resource_path("src/img/GASEL_R_QUIMICA_TRANSPARENTE.png")
    logo_photo = resize_image(logo_path, 200)
    icon = ctk.CTkLabel(master=aside, image=logo_photo, text="")
    icon.image = logo_photo  # Keep a reference!
    icon.pack(pady=(50, 20), padx=20)

    return aside

def add_switch_control(aside, switch_event_handler):
    """Add switch control to sidebar for database enable/disable."""
    switch_var = ctk.StringVar(value="on")
    switchBD = ctk.CTkSwitch(master=aside, text="Habilitar Base de Datos", variable=switch_var,
                            onvalue="on", offvalue="off", command=lambda: switch_event_handler(switch_var))
    switchBD.pack(pady=10, padx=10, side="bottom")
    return switch_var

def add_navigation_buttons(aside, switch_panel_function):
    """Add navigation buttons to the sidebar."""
    home_button = ctk.CTkButton(master=aside, text="Home", fg_color="#343638", hover_color="#565B5E", text_color="white",
                                command=lambda: switch_panel_function(create_home_panel))  # Home panel doesn't need the switch_var
    home_button.pack(pady=10, padx=10, fill="x")
    admin_view = False
    precursor_control_button = ctk.CTkButton(master=aside, text="Control de Precursores", fg_color="#343638", hover_color="#565B5E", text_color="white",
                                            command=lambda: switch_panel_function(create_precursor_control_panel))
    precursor_control_button.pack(pady=10, padx=10, fill="x")

# ---------------------------------------------------------------
# Main GUI Setup
# ---------------------------------------------------------------

def run_guest_view():
    """Create and run the admin dashboard."""
    app = ctk.CTk()
    app.geometry("1280x720")
    
    app.title("Invitado Dashboard")

    aside = setup_sidebar(app)
    switch_var = add_switch_control(aside, switch_event)
    main_panel = ctk.CTkScrollableFrame(master=app, fg_color="transparent")
    main_panel.pack(side="right", fill="both", expand=True)
    
    content_panel = ctk.CTkFrame(master=main_panel, fg_color="transparent")
    content_panel.pack(padx=50, pady=(0,50), fill="both", expand=True)

    def switch_panel(panel_function, admin_view =False):
        """Clear content panel and add new content."""
        for widget in content_panel.winfo_children():
            widget.destroy()
        if panel_function == create_precursor_control_panel:            
            panel_function(content_panel, switch_var, False)  # Pass the switch_var to panel functions
        else:
            panel_function(content_panel, switch_var) 

    add_navigation_buttons(aside, switch_panel)
    switch_panel(create_home_panel)  # Initialize with the home panel

    return app  # Return the app instance for further manipulation if needed

if __name__ == "__main__":
    run_guest_view()
