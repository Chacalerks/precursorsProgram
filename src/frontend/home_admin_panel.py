import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import Canvas
from frontend.utilitiesFun import resource_path, getLabs, getMonths, getYears, getCurrentMonthYear, clear_frame
import tkinter as tk
from functions import checkLabsReportOnMonth, loadCollection,createMonthInform, writeSummedSubstances
from tkinter import messagebox


def create_info_card(parent, photo_image, label_text, value_text, icon_size=(100, 100)):
    card = ctk.CTkFrame(master=parent, corner_radius=10, fg_color="#333333")
    # Resize the icon as per the size provided
    resized_image = photo_image.resize(icon_size, Image.Resampling.LANCZOS)  # Updated to use LANCZOS resampling
    photo_image = ImageTk.PhotoImage(resized_image)
    
    icon = ctk.CTkLabel(master=card, image=photo_image, text="")
    icon.image = photo_image  # Keep a reference!
    icon.pack(side="left", padx=10, pady=10)

    # Container for text to align it next to the icon
    text_container = ctk.CTkFrame(master=card, fg_color="transparent")
    text_container.pack(padx=20, pady=30, side="left", fill="both", expand=True)
    label = ctk.CTkLabel(master=text_container, text=label_text, font=("Roboto", 20, "bold"))
    label.pack(pady=(0,10),side="top", anchor="w")
    value_label = ctk.CTkLabel(master=text_container, text=value_text, font=("Roboto", 16))
    value_label.pack(side="top", anchor="w")
    
    return card

def on_label_click(event, label_text, report):
    if report == False:
        messagebox.showinfo("Message", "Hello, this is a message box!")
    else:
        writeSummedSubstances(report["substances"])

def create_month_list_report(parent, photo_image, label_text, report, icon_size=(25, 25)):
    monthElement = ctk.CTkFrame(master=parent, corner_radius=10, fg_color="transparent")
    text_container = ctk.CTkFrame(master=monthElement, fg_color="transparent")
    text_container.pack(pady=(0,5), padx=10, side="top", fill="both", expand=True)
    
    # Resize the icon as per the size provided
    resized_image = photo_image.resize(icon_size, Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(resized_image)
    
    label = ctk.CTkLabel(master=text_container, text=label_text, font=("Roboto", 12, "bold"))
    label.pack(pady=0, side="left", anchor="w")
    
    icon = ctk.CTkLabel(master=text_container, image=photo_image, text="")
    icon.image = photo_image  # Keep a reference!
    icon.pack(pady=0, side="right", padx=10, anchor="w")
    
    # Crear un Canvas para la línea divisoria
    line_canvas = Canvas(monthElement, height=1, bg='gray', highlightthickness=0)
    line_canvas.pack(pady=0,fill='x', side="bottom", padx=10)
    
    icon.bind("<Button-1>", lambda event, lt=label_text: on_label_click(event, lt, report))


    return monthElement

def create_labs_list_report(parent, photo_image, label_text, icon_size=(25, 25)):
    monthElement = ctk.CTkFrame(master=parent, corner_radius=10, fg_color="transparent")
    text_container = ctk.CTkFrame(master=monthElement, fg_color="transparent")
    text_container.pack(pady=(0,5), padx=10, side="top", fill="both", expand=True)
    
    # Resize the icon as per the size provided
    resized_image = photo_image.resize(icon_size, Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(resized_image)
    
    label = ctk.CTkLabel(master=text_container, text=label_text, font=("Roboto", 12, "bold"))
    label.pack(pady=0, side="left", anchor="w")
    
    icon = ctk.CTkLabel(master=text_container, image=photo_image, text="")
    icon.image = photo_image  # Keep a reference!
    icon.pack(pady=0, side="right", padx=10, anchor="w")
    
    # Crear un Canvas para la línea divisoria
    line_canvas = Canvas(monthElement, height=1, bg='gray', highlightthickness=0)
    line_canvas.pack(pady=0,fill='x', side="bottom", padx=10)
    
    icon.bind("<Button-1>", lambda event, lt=label_text: on_label_click(event, lt))


    return monthElement


    
    

def create_home_panel(parent, asdf):
    title_label = ctk.CTkLabel(master=parent, text="Reportes y Datos", font=("Roboto", 24), anchor="w")
    title_label.pack(pady=(40, 20), padx=20, fill="x")

    cards_container = ctk.CTkFrame(master=parent, fg_color="transparent")
    cards_container.pack(pady=10, padx=20, fill="x")

    # Load image for icons
    iconPath = resource_path("src/img/flask.png")
    iconImage = Image.open(iconPath)

    # Create cards with images
    card1 = create_info_card(cards_container, iconImage, "Mayor Elemento en Inventario", "Alcohol Etílico")
    card1.pack(side="left", padx=(0,30), fill="y")

    card2 = create_info_card(cards_container, iconImage, "Menor Elemento en Inventario", "Anhídrido acético")
    card2.pack(side="left", padx=(0,30), fill="y")

    # ---------------------------------------------------- List of Months and Labs
    report_container = ctk.CTkFrame(master=parent, fg_color="transparent")
    report_container.pack( pady=10, padx=20, fill="x")
    
    loadCollection()
    
    #------------------------ reports by month   
    month_report_container = ctk.CTkFrame(master=report_container)
    month_report_container.pack(side="left", padx=(0,20), fill="y")
    
    text_header_month_report_container = ctk.CTkFrame(master=month_report_container, fg_color="transparent")
    text_header_month_report_container.pack(side="top", padx=20, fill="both", expand=True)
    
    label = ctk.CTkLabel(master=text_header_month_report_container, text="Año a consultar: ", font=("Roboto", 14, "bold"))
    label.pack(pady=0, side="left", anchor="w")

    def combobox_callback(choice):
        loadCollection()
        monthReport = []
        for i in monthArray:            
            monthReport.append(createMonthInform(i, choice))

    
    currentYear, currentMonthIndex = getCurrentMonthYear()

    yearComboBoxValues = getYears()
    #--- load month list
    monthArray = getMonths()
    labs = getLabs()
    
    yearComboBox = ctk.CTkComboBox(master=text_header_month_report_container, values=yearComboBoxValues,
                                        command=combobox_callback)
    
    yearComboBox.set(str(currentYear))
    yearComboBox.pack(side="right", pady=(5,10))
    
    # Load image for icons
    excelIconPath = resource_path("src/img/excel.png")
    excelIconImage = Image.open(excelIconPath)
    
    
    list_month_container = ctk.CTkFrame(master=month_report_container, fg_color="transparent")
    list_month_container.pack(padx=(0,20), fill="y") 
    
    # ----get
    monthReport = []
    for i in monthArray:            
        monthReport.append(createMonthInform(i, currentYear))
        
    def load_month_report():        
        elements = []
        index = 0
        for i in monthArray:
            # Load image for icons
            valueReport = monthReport[index]
            if valueReport != False:
                excelIconPath = resource_path("src/img/excel.png")
            else:
                excelIconPath = resource_path("src/img/excel_transparent.png")
            excelIconImage = Image.open(excelIconPath)
            element = create_month_list_report(list_month_container,excelIconImage, i, valueReport)
            element.pack()        
            elements.append(element)
            index +=1
    
    load_month_report()
    #------------------------ reports by Labs
    labs_report_container = ctk.CTkFrame(master=report_container, corner_radius=10)
    labs_report_container.pack(side="left", fill="both")
    
    # --- containers
    text_header_lab_report_container = ctk.CTkFrame(master=labs_report_container, fg_color="transparent")
    text_header_lab_report_container.pack(side="top", padx=20, fill="x", expand=True)
    
    lab_list_report_container = ctk.CTkFrame(master=labs_report_container, fg_color="transparent")
    lab_list_report_container.pack(side="top", padx=20, fill="both", expand=True)
    
    # --- text_header_lab_report_container elements
    label = ctk.CTkLabel(master=text_header_lab_report_container, text="Mes a Consultar: ", font=("Roboto", 14, "bold"))
    label.pack(pady=0, side="left", anchor="w")
    
    def monthCombobox_callback(choice):        
        labsElements = []
        clear_frame(scrollable_frame)
        loadCollection()
        for i in labs:
            report = checkLabsReportOnMonth(choice, i)
            if report == False:
                statusIcon = resource_path("src/img/cancel.png")
            else:
                statusIcon = resource_path("src/img/accept.png")
            statusIconImage = Image.open(statusIcon)
            
            element = create_labs_list_report(scrollable_frame,statusIconImage, i)
            element.pack()        
            labsElements.append(element)
    
    currentYear, currentMonthIndex = getCurrentMonthYear()

    monthsComboBoxValues = monthArray
    monthComboBox = ctk.CTkComboBox(master=text_header_lab_report_container, values=monthsComboBoxValues,
                                        command=monthCombobox_callback)
    
    monthComboBox.set(monthsComboBoxValues[currentMonthIndex])
    monthComboBox.pack(side="right", pady=(5,10))
    
    # --- lab_list_report_container elements       
    canvas = Canvas(lab_list_report_container, background="#333333")
    scrollbar = tk.Scrollbar(lab_list_report_container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the scrollbar to the right, fill in the y-direction
    scrollbar.pack(side="right", fill="y")
    # Pack the canvas to expand and fill both directions
    canvas.pack(side="left",pady=0, padx=(0,23), fill="y", expand=True)

    # Create a CTkFrame that will contain the content
    scrollable_frame = ctk.CTkFrame(lab_list_report_container)
    
    # Create a window on the canvas to hold the scrollable_frame
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    labs = getLabs()
    labsElements = []
    
    for i in labs:
        report_by_instance = checkLabsReportOnMonth(monthArray[currentMonthIndex], i)
        if report_by_instance == False:
            statusIcon = resource_path("src/img/cancel.png")
        else:
            statusIcon = resource_path("src/img/accept.png")
        statusIconImage = Image.open(statusIcon)
        
        element = create_labs_list_report(scrollable_frame,statusIconImage, i)
        element.pack()        
        labsElements.append(element)
        

        
    # Function to update the scrolling region to all of the canvas
    def on_frame_configure(event):
        # Update the scroll region to encompass the inner frame
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind the configuration event of the scrollable_frame to on_frame_configure
    scrollable_frame.bind("<Configure>", on_frame_configure)

    
    
    
    
    
