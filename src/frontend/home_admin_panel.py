# home_admin_panel.py
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import Canvas, messagebox
import tkinter as tk
from frontend.utilitiesFun import resource_path, getLabs, getMonths, getYears, getCurrentMonthYear, clear_frame
from functions import check_labs_report_on_month, load_collection, create_monthly_report, writeSummedSubstances, check_month_report
from tkinter import Canvas, Scrollbar, Frame, Text
# ---------------------------------------------------------------
# Initialization
# ---------------------------------------------------------------

load_collection()  

# ---------------------------------------------------------------
# Utility Functions
# ---------------------------------------------------------------

def create_info_card(parent, photo_image, label_text, value_text, icon_size=(100, 100)):
    """Create and return an information card with an icon and text."""
    resized_image = photo_image.resize(icon_size, Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(resized_image)

    # ------------------- Container card
    card = ctk.CTkFrame(master=parent, corner_radius=10, fg_color="#333333")
    icon = ctk.CTkLabel(master=card, image=photo_image, text="")
    icon.image = photo_image  # Keep a reference!
    icon.pack(side="left", padx=10, pady=10)
    
    # ------------------- Container text_container
    text_container = ctk.CTkFrame(master=card, fg_color="transparent")
    text_container.pack(padx=20, pady=30, side="left", fill="both", expand=True)
    # Elements of text_container
    label = ctk.CTkLabel(master=text_container, text=label_text, font=("Roboto", 20, "bold"))
    label.pack(pady=(0, 10), side="top", anchor="w")
    value_label = ctk.CTkLabel(master=text_container, text=value_text, font=("Roboto", 16))
    value_label.pack(side="top", anchor="w")

    return card

# ---------------------------------------------------------------
# Event Handlers
# ---------------------------------------------------------------

def on_click_excel_icon(event, label_text, year, report):
    """Handle clicks on labels which may trigger additional actions."""
    try:
        if not report:
            messagebox.showinfo("Message", "Hello, this is a message box!")
        else:
            writeSummedSubstances(report["substances"], label_text+str(year))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# ---------------------------------------------------------------
# Detailed Report Setup Functions
# ---------------------------------------------------------------

def create_month_list_report(parent, photo_image, label_text,year, report, icon_size=(25, 25)):
    """Create and return a single month report element with an icon and text."""
    month_element = ctk.CTkFrame(master=parent, corner_radius=10, fg_color="transparent")
    month_element.pack(fill="both", expand=True)
    
    text_container = ctk.CTkFrame(master=month_element, fg_color="transparent")
    text_container.pack(pady=(0,5), padx=10, side="top", fill="both", expand=True)

    resized_image = photo_image.resize(icon_size, Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(resized_image)
    
    label = ctk.CTkLabel(master=text_container, text=label_text, font=("Roboto", 12, "bold"))
    label.pack(pady=0, side="left", anchor="w")
    
    icon = ctk.CTkLabel(master=text_container, image=photo_image, text="")
    icon.image = photo_image  # Keep a reference!
    icon.pack(pady=0, side="right", padx=10, anchor="w")
    
    line_canvas = Canvas(month_element, height=1, bg='gray', highlightthickness=0)
    line_canvas.pack(pady=0, fill='x', side="bottom", padx=10)
    
    icon.bind("<Button-1>", lambda event, lt=label_text: on_click_excel_icon(event, lt,year, report))

    return month_element

def create_labs_list_report(parent, photo_image, label_text, icon_size=(25, 25)):
    """Create and return a single lab report element with an icon and text."""
    lab_element = ctk.CTkFrame(master=parent, corner_radius=10, fg_color="transparent")
    lab_element.pack(fill="both", expand=True)
    
    text_container = ctk.CTkFrame(master=lab_element, fg_color="transparent")
    text_container.pack(pady=(0,5), padx=10, side="top", fill="both", expand=True)

    resized_image = photo_image.resize(icon_size, Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(resized_image)
    
    label = ctk.CTkLabel(master=text_container, text=label_text, font=("Roboto", 12, "bold"))
    label.pack(pady=0, side="left", anchor="w")
    
    icon = ctk.CTkLabel(master=text_container, image=photo_image, text="")
    icon.image = photo_image  # Keep a reference!
    icon.pack(pady=0, side="right", padx=10, anchor="w")
    
    line_canvas = Canvas(lab_element, height=1, bg='gray', highlightthickness=0)
    line_canvas.pack(pady=0, fill='x', side="bottom", padx=10)
    
    return lab_element


# ---------------------------------------------------------------
# Specific Report Setup Functions
# ---------------------------------------------------------------

def setup_month_reports(container, year):
    """Setup and populate month reports in their designated container."""
    clear_frame(container)  # Clear existing content in the container
    try:
        months = getMonths()
        
        for i in months:
            report = check_month_report(i, year)
            icon_path = resource_path("src/img/excel.png" if report else "src/img/excel_transparent.png")
            excel_icon_image = Image.open(icon_path)
            month_element = create_month_list_report(container, excel_icon_image, i, year, report, icon_size=(25, 25))
            month_element.pack(pady=(0, 10), fill='x', expand=True)
        
        
        

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load initial month reports: {str(e)}")


def setup_lab_reports(container, month, currentYear):
    """Setup and populate lab reports in their designated container."""
    clear_frame(container)  # Clear existing content in the container
    try:
        labs = getLabs()
        for lab in labs:            
            report = check_labs_report_on_month(month, lab, currentYear)
            icon_path = resource_path("src/img/accept.png") if report else resource_path("src/img/cancel.png")
            create_labs_list_report(container, Image.open(icon_path), lab).pack()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load lab reports: {str(e)}")
        

# ---------------------------------------------------------------
# Panel Creation Functions
# ---------------------------------------------------------------
def create_home_panel(parent, _):
    """Create the main home panel with reports and data."""
    title_label = ctk.CTkLabel(master=parent, text="Reportes y Datos", font=("Roboto", 24), anchor="w")
    title_label.pack(pady=(40, 20), padx=20, fill="x")

    cards_container = ctk.CTkFrame(master=parent, fg_color="transparent")
    cards_container.pack(pady=5, padx=20, fill="x", expand=True)

    icon_image = Image.open(resource_path("src/img/flask.png"))
    card1 = create_info_card(cards_container, icon_image, "Mayor Elemento en Inventario", "Alcohol Etílico")
    card1.pack(side="left", padx=(0, 30), fill="y")
    card2 = create_info_card(cards_container, icon_image, "Menor Elemento en Inventario", "Anhídrido acético")
    card2.pack(side="left", padx=(0, 30), fill="y")

    # ------------------- Container report_container 
    report_container = ctk.CTkFrame(master=parent, fg_color="transparent")
    report_container.pack(pady=(10, 5), padx=20, fill="both", expand=True)  
    currentYear, currentMonthIndex = getCurrentMonthYear()
    months = getMonths()

    # ------------------- Container month_report_container
    month_report_container = ctk.CTkFrame(master=report_container)
    month_report_container.pack(side="left", padx=(0, 20), fill="both", expand=True)


    # Container header_container (text, combobox)
    header_container = ctk.CTkFrame(master=month_report_container, fg_color="transparent")
    header_container.pack(padx=20, pady=(25, 0), fill="x", expand=True)
    # Label for the combo box
    year_label = ctk.CTkLabel(master=header_container, text="Año a consultar: ", font=("Roboto", 14, "bold"))
    year_label.pack(side="left", anchor="w")
    # Combo box to select the year
    yearComboBox = ctk.CTkComboBox(master=header_container, values=getYears())
    yearComboBox.set(str(currentYear))  # Set the current year as default
    yearComboBox.pack(side="right", fill="x", expand=True)
    # Attach the callback to update reports based on selected year
    yearComboBox.configure(command=lambda choice: setup_month_reports(scrollableFrameListMonths, choice))
    # Container header_container (text, combobox)
    scrollableFrameListMonths = ctk.CTkScrollableFrame(master=month_report_container, height=350, fg_color="transparent")
    scrollableFrameListMonths.pack(padx=20, pady=10, fill="both", expand=True)
    
    # -------------------------------------- Container labs_report_container
    labs_report_container = ctk.CTkFrame(master=report_container, corner_radius=10)
    labs_report_container.pack(side="left", fill="both", expand=True)
    
    # Container header_container (text, combobox)
    header_container2 = ctk.CTkFrame(master=labs_report_container, fg_color="transparent")
    header_container2.pack(padx=20, pady=(20, 10), fill="x", expand=True)
    # Label for the combo box
    month_label = ctk.CTkLabel(master=header_container2, text="Mes a consultar: ", font=("Roboto", 14, "bold"))
    month_label.pack(side="left", anchor="w")
    # Combo box to select the year
    monthComboBox = ctk.CTkComboBox(master=header_container2, values=months)
    monthComboBox.set(months[currentMonthIndex])  # Set the current month as default
    monthComboBox.pack(side="right", fill="x", expand=True)
    # Attach the callback to update reports based on selected month
    monthComboBox.configure(command=lambda choice: setup_lab_reports(scrollableFrameListLabs, choice, currentYear))
    # Container header_container (text, combobox)
    scrollableFrameListLabs = ctk.CTkScrollableFrame(master=labs_report_container, height=350, fg_color="transparent")
    scrollableFrameListLabs.pack(padx=20, pady=10, fill="both", expand=True)
    
    
    # Set up month and lab report sections
    setup_month_reports(scrollableFrameListMonths, currentYear)
    setup_lab_reports(scrollableFrameListLabs, months[currentMonthIndex], currentYear)





