from openpyxl import load_workbook, Workbook
from tools import openFileExplorer, writeSummedSubstances
from substance import Substance
from db import MongoDB
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def createReport(substances,instance, month, year):
    report = {}   
    # assign the instance, month and year to the report
    report["instance"] = instance
    report["month"] = month
    report["year"] = year
    
    
    # create an array for the substances
    substancesArray = []
    # assing the substances to the array
    for key in substances:
        substancesArray.append(substances[key].__dict__)
    # assign the array to the report
    report["substances"] = substancesArray
    
    # assing the date now to the report
    report["date"] = datetime.now()
    
    #insert the report to the database
    mongo = MongoDB()
    mongo.insert_monthly_report(report)
    
    #print(report)
    
def processFiles():
    substances = {}
    filesPaths = openFileExplorer()
    
    for file in filesPaths:
        wb = load_workbook(file, data_only=True)
        sheet = wb.active
        
        # get the instace in the row 4 and column 3
        instance = sheet.cell(row=4, column=3).value
        
        # get the month in the row 3 and column 3
        month = sheet.cell(row=3, column=3).value
        
        # get the year in the row 3 and column 13
        year = sheet.cell(row=3, column=13).value
        
        print(instance, month, year)
        
        flag = True
        
        for row in sheet.iter_rows(min_row=1, values_only=True):
            #print(row)
            if not ("Lista" in str(row[1])) and row[3] != "-":
                quimic = Substance(row[1],  # Name
                row[2],  # Unity Measure
                row[6],  # Inventory Additions in KG
                row[7],  # Addition Number
                row[9],  # Inventory Expenses in KG
                row[10], # Final Balance
                row[12]) # Expense Justification
                
                
                
                if quimic.name in substances:
                    
                    substances[quimic.name].update(quimic)
                else:
                    
                    substances[quimic.name] = quimic
        
                   

        wb.close()
    createReport(substances,instance, month, year)
    #writeSummedSubstances(substances)

# Function to call the message box
def show_message(msg):
    messagebox.showinfo(msg)