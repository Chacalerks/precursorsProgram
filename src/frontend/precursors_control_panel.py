import customtkinter as ctk
from tkinter import filedialog
from functions import process_files



def printPicah(switchBD_var):
    print("switch toggled, current value desde picha:", switchBD_var.get())

def create_precursor_control_panel(parent,switchBD_var, admin_view = True):
    print("El admin view es> ",admin_view)
    # Title for the section
    title_label = ctk.CTkLabel(master=parent, text="Control de Precursores", font=("Roboto", 16))
    title_label.pack(pady=(10, 20))
    if admin_view:        
        # Frame for the search panel
        search_panel = ctk.CTkFrame(master=parent, corner_radius=10)
        search_panel.pack(pady=20, padx=20, fill="x")

        # Entry for search
        search_entry = ctk.CTkEntry(master=search_panel, placeholder_text="Search...", width=200)
        search_entry.pack(side="left", padx=(10, 5), pady=10)

        # Search button
        search_button = ctk.CTkButton(master=search_panel, text="Search", width=100)
        search_button.pack(side="left", padx=(5, 10), pady=10)

        # Frame for the table (Placeholder for actual table implementation)
        table_container = ctk.CTkFrame(master=parent, corner_radius=10)
        table_container.pack(pady=(0, 20), padx=20, fill="both", expand=True)
        # Dummy text for table, replace with actual table widget
        table_label = ctk.CTkLabel(master=table_container, text="Table will be loaded here", font=("Roboto", 12))
        table_label.pack(padx=20, pady=20)

    # Drag and Drop File Upload Area
    file_upload_area = ctk.CTkFrame(master=parent, corner_radius=10)
    file_upload_area.pack(pady=20, padx=20, fill="x")
    file_upload_label = ctk.CTkLabel(master=file_upload_area, text="Drag & Drop to Upload File",
                                    fg_color="transparent", bg_color="#4C5C68", height=100)
    file_upload_label.pack(fill="both", expand=True)
    file_upload_label.bind("<Button-1>", lambda e: process_files(switchBD_var.get(), admin_view))
    
    


