import csv
from datetime import datetime
from PIL import Image, ImageTk
from dotenv import load_dotenv
import os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    import sys, os
    if getattr(sys, 'frozen', False):
        # we are running in a |PyInstaller| bundle
        base_path = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        base_path = os.path.abspath(".")
    
    full_path = os.path.join(base_path, relative_path)
    print(f'Resource path: {full_path}')  # Debugging output
    return full_path


# Path to the CSV file
def getLabs():
    filename = 'src/data/labs.csv'
    filename = resource_path(filename)
    # Array to hold the data
    data = []

    # Open the CSV file and read the data
    with open(filename, newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object specifying the delimiter as semicolon
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:           
            # Each row is read as a list of strings
            data = row
    return data

def getMonths():
    filename = 'src/data/months.csv'
    filename = resource_path(filename)
    # Array to hold the data
    data = []

    # Open the CSV file and read the data
    with open(filename, newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object specifying the delimiter as semicolon
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            # Each row is read as a list of strings
            data = row
    return data

def getYears():
    filename = 'src/data/years.csv'
    filename = resource_path(filename)
    # Array to hold the data
    data = []

    # Open the CSV file and read the data
    with open(filename, newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object specifying the delimiter as semicolon
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            # Each row is read as a list of strings
            data = row
    return data


import datetime

def getCurrentMonthYear():
    # Get the current year and month
    current_date = datetime.datetime.now()
    current_year = current_date.year
    current_month = current_date.month

    # Get the index of the current month (0-based)
    month_index = current_month - 1  # January is 0, February is 1, etc.

    return current_year, month_index

def clear_frame(frame):
    # This function will destroy all widgets in the frame, effectively clearing it.
    for widget in frame.winfo_children():
        widget.destroy()
        
def resize_image(image_path, new_width):
    """Resize an image while maintaining its aspect ratio."""
    image = Image.open(image_path)
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    new_height = int(new_width / aspect_ratio)
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)

def load_environment_vars():
    """Load environment variables from the .env file."""
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(env_path)
