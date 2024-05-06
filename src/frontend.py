import tkinter as tk
from tkinter import messagebox, Listbox, END
from functions import processFiles
from db import MongoDB  # Import the MongoDB connection class

def fetch_reports():
    """Fetch monthly reports from the database and return a list of report names."""
    mongo_db = MongoDB()  # Create an instance of MongoDB connection
    reports = mongo_db.find_reports_by_month_year("Febrero", 2024)
    return reports
    

def populate_listbox(listbox):
    """Populate the listbox with monthly report names."""
    try:
        reports = fetch_reports()
        listbox.delete(0, END)  # Clear the listbox
        for report in reports:
            listbox.insert(END, report)  # Insert each report into the listbox
    except Exception as e:
        messagebox.showerror("Database Connection Error", str(e))

def setup_gui():
    root = tk.Tk()
    root.title("Tkinter Application")
    root.geometry('700x500')  # Adjusted for additional UI elements

    # Creating a Listbox to display the monthly reports
    listbox = Listbox(root, height=10, width=50)
    listbox.pack(pady=20)

    # Button to refresh the list of monthly reports
    btn_refresh = tk.Button(root, text="Refresh Reports", command=lambda: populate_listbox(listbox))
    btn_refresh.pack(pady=10)

    # Button to open files and compile substances
    btn_open_file = tk.Button(root, text="Open Excel Files and Compile Substances", command=processFiles)
    btn_open_file.pack(pady=20)

    populate_listbox(listbox)  # Initial population of the listbox

    return root

def run_gui():
    root = setup_gui()
    root.mainloop()
