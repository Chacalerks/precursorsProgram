from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, PatternFill, Font
from openpyxl import Workbook
from tkinter import filedialog


def openFileExplorer():
    filetypes = (('Excel files', '*.xlsx *.xls *.xlsm'), ('All files', '*.*'))
    filepaths = filedialog.askopenfilenames(title='Open files', initialdir='.', filetypes=filetypes)
    return filepaths

def writeSummedSubstances(substances):
    wb = Workbook()
    ws = wb.active

    # Load and insert the logo image
    img = Image('logo.png')  # Make sure 'logo.png' is in your working directory
    ws.merge_cells('A1:C1')  # Merge for the logo
    ws.add_image(img, 'A1')

    # Setting row heights
    ws.row_dimensions[1].height = 50  # First row height
    ws.row_dimensions[2].height = 2   # Second row height

    # Merging cells for the header
    ws.merge_cells('D1:F1')  # Merge for the title "Reporte de Precursores"
    ws['D1'] = 'Reporte de Precursores'
    ws['D1'].alignment = Alignment(horizontal='center', vertical='center')

    ws['G1'] = 'Código: F-06-RQ-TEC'
    ws['G1'].alignment = Alignment(horizontal='center', vertical='center')

    ws.merge_cells('A2:G2')  # Merge for the second row to create space

    # Column headers
    columns = ["Sustancia", "Unidad", "Ingreso Período", "# Solicitud de Bienes", "Despacho Período", "Existencias Final Período", "Uso dado a la Sustancia"]
    ws.append(columns)

    # Setting style for the header row
    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")  # Dark blue background
    font_white = Font(color="FFFFFF")  # White font

    for cell in ws[3]:  # Third row has the headers
        cell.fill = header_fill
        cell.font = font_white
    ws.row_dimensions[3].height = 45  # Third row height

    # Adjusting widths for the columns
    width_name = 30
    width_use = 60
    count = 0
    for col in ws.columns:
        if count == 0:
            ws.column_dimensions[col[2].column_letter].width = width_name
        elif count == 6:
            ws.column_dimensions[col[2].column_letter].width = width_use
        else:            
            max_length = max(len(str(cell.value)) for cell in col)
            adjusted_width = max_length + 2  # Adding some extra padding
            ws.column_dimensions[col[2].column_letter].width = adjusted_width
        count += 1

    for substance in substances.values():
        row = [substance.name, substance.unityMeasure, substance.inventoryAdditions, substance.additionNumber, substance.inventoryExpenses, substance.finalBalance, substance.expenseJustification]
        ws.append(row)

        # Adjusting text alignment and enabling text wrap for better readability
        for cell in ws[ws.max_row]:
            cell.alignment = Alignment(horizontal='center', vertical='center', wrapText=True)
            ws.row_dimensions[ws.max_row].height = 30  # Set the height for other rows

    wb.save("Compiled_Substances_Summed.xlsx")

