import customtkinter as ctk
from .home_admin_panel import create_home_panel
from .precursors_control_panel import create_precurso_control_panel

def run_admin_view():
    app = ctk.CTk()
    app.geometry("1280x720")
    app.title("Admin Dashboard")

    aside = ctk.CTkFrame(master=app, width=200, corner_radius=0)
    aside.pack(side="left", fill="y")

    content_panel = ctk.CTkFrame(master=app, fg_color="transparent")
    content_panel.pack(side="right", fill="both", expand=True)

    # Define a function to clear the content panel and add new content
    def switch_panel(panel_function):
        for widget in content_panel.winfo_children():
            widget.destroy()
        panel_function(content_panel)

    # Sidebar buttons
    home_button = ctk.CTkButton(master=aside, text="Home", fg_color="#343638", hover_color="#565B5E", text_color="white",
                                command=lambda: switch_panel(create_home_panel))
    home_button.pack(pady=10, padx=10, fill="x")

    precurso_control_button = ctk.CTkButton(master=aside, text="Precurso Control", fg_color="#343638", hover_color="#565B5E", text_color="white",
                                            command=lambda: switch_panel(create_precurso_control_panel))
    precurso_control_button.pack(pady=10, padx=10, fill="x")

    # Initialize with the home panel
    switch_panel(create_home_panel)

    return app  # Return the app instance for further manipulation if needed
