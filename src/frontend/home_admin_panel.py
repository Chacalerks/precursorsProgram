import customtkinter as ctk

def create_home_panel(parent):
    label = ctk.CTkLabel(master=parent, text="This is the Home panel")
    label.pack(pady=20, padx=20)
