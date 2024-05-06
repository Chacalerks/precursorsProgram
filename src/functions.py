from openpyxl import load_workbook, Workbook
from tools import openFileExplorer, writeSummedSubstances
from substance import Substance
from db import MongoDB
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from frontend.utilitiesFun import getMonths, getLabs

db = MongoDB()
def loadCollection():
    global db
    db.get_month_reports()


def createReportbyInstance(substances, report):    
    global db
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
    
    db.insert_monthly_report_by_instance(report)

def checkLabsReportOnMonth(month, instance, year= 2024):
    global db
    
    #picha = db.find_reports_by_month_instance(month, instance)
    #print(picha)
    
    report = list(db.month_report_by_instance.find({"year": year,"month": month, "instance": instance}, {"_id": 0})) #db.find_reports_by_month_instance(month, instance)
    if report != []:
        return report[0]
    else:
        return False
    
    
def createMonthInform(month, year):
    report = {}
    global db
    substances = {}
    year = int(year)
    r = list(db.month_report_by_instance.find({"year": year,"month": month}, {"_id": 0}))
    if not r ==  None:
        if not r == []:
            for i in r:
                for j in i["substances"]:
                    quimic = Substance(j["name"],  # Name
                            j["unityMeasure"],  # Unity Measure row 2 in the excel
                            j["inventoryAdditions"],  # Inventory Additions KG
                            j["additionNumber"],  # Addition Number
                            j["inventoryExpenses"],  # Inventory Expenses KG
                            j["finalBalance"], # Final Balance (assuming this is what you intend)
                            j["expenseJustification"]) # Expense Justification
                    if quimic.name in substances:                    
                        substances[quimic.name].update(quimic)
                    else:                    
                        substances[quimic.name] = quimic
    report["month"] = month
    report["year"] = year
    report["dateCreated"] = datetime.now()
    
    substancesArray = []
    # assing the substances to the array
    for key in substances:
        substancesArray.append(substances[key].__dict__)
    # assign the array to the report
    report["substances"] = substancesArray
    
    if len(substances) >0:
        db.insert_monthly_report(report)
        return report
    return False
    
def processFiles(switchBD):
    substances = {}
    filesPaths = openFileExplorer()
    
    for file in filesPaths:
        wb = load_workbook(file, data_only=True)
        sheet = wb.active
        report = {} 
        substancesTemp = {}
        # iterate over all quimic substance
        for row in sheet.iter_rows(min_row=12, values_only=True):
            if not ("Lista" in str(row[1])) and row[3] != "-":
                quimic = Substance(row[1],  # Name
                    "Kg",  # Unity Measure row 2 in the excel
                    row[6],  # Inventory Additions KG
                    row[7],  # Addition Number
                    row[9],  # Inventory Expenses KG
                    row[11], # Final Balance (assuming this is what you intend)
                    row[12]) # Expense Justification

                substancesTemp[quimic.name] = quimic
                
                if quimic.name in substances:                    
                    substances[quimic.name].update(quimic)
                else:                    
                    substances[quimic.name] = quimic
        

        if switchBD == "on":
            # assign the instance, month and year to the report
            report["instance"] = sheet.cell(row=6, column=3).value  # get the instace
            report["year"] = sheet.cell(row=4, column=3).value  # get the year
            report["month"] = sheet.cell(row=5, column=3).value # get the month           
            report["personAssigned"] = sheet.cell(row=7, column=3).value  # get the personAssign
            report["email"] = sheet.cell(row=8, column=3).value  # get the email
            report["phoneNumber"] = sheet.cell(row=9, column=3).value  # get the phone  
            createReportbyInstance(substancesTemp,report)
            
        wb.close()
        
    # Write the summed substances to a new Excel file
    writeSummedSubstances(substances)


# Function to call the message box
def show_message(msg):
    messagebox.showinfo(msg)