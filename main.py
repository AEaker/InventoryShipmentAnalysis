from tkinter.filedialog import askopenfilename
import tkinter.messagebox
import pandas as pd
import pandas.io.formats.excel
import numpy as np
import xlsxwriter
# import argparse
import tkinter as tk
from CleanData import CullInvReport, AllocationsForecastAndSupply, get_col_widths
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

root = tk.Tk()
#get rid of window
root.withdraw()
print("Correlating Paths")
# parser = argparse.ArgumentParser()
# parser.add_argument("-c", "--count", required=True, help="Path to part history/count to grab dataset")
# parser.add_argument("-i", "--ideal", required=True, help="Path to ideal parameter file. First two columns should be named Part Number and Description")
# parser.add_argument("-o", "--output", help="Path to Store Output") 
# args = parser.parse_args()
print("Need Inventory Count")
tk.messagebox.showinfo(title="Inventory Count", message="Select Inventory Count file.")
PartCount = askopenfilename()
CompletedServicesDF = pd.read_excel(PartCount)
print("Need Ideal specs")
tk.messagebox.showinfo(title="Ideal Space", message="Select the 'ideal' max inventory space file.")
idealfile = askopenfilename()
ideal = pd.read_excel(idealfile)

mergedf = CullInvReport(CompletedServicesDF, ideal)
print("Need forecast")
tk.messagebox.showinfo(title="Forecast", message="Select the Forecast file.")
forecastfile = askopenfilename()
Forecast = pd.read_excel(forecastfile, sheet_name="WIP")
print("Need allocation direction")
tk.messagebox.showinfo(title="Allocations", message="Select the Allocations file.")
allocationfile = askopenfilename()
Allocations = pd.read_excel(allocationfile)


UpdatedDF = AllocationsForecastAndSupply(Allocations, Forecast, mergedf)

writer = pd.ExcelWriter("ShipmentPrediction.xlsx", engine='xlsxwriter', options={'strings_to_formulas': False}) 
UpdatedDF.to_excel(writer, sheet_name="Summary", index=False)
workbook = xlsxwriter.Workbook("ShipmentPrediction.xlsx")
worksheet = writer.sheets["Summary"]



worksheet.set_column("A:A", 17)
worksheet.set_column("B:B", 37)
worksheet.set_column("C:C", 8)
worksheet.set_column("D:E", 12)
worksheet.set_column("F:F", 17)
worksheet.set_column("G:H", 10.5)
worksheet.set_column("I:I", 20)
worksheet.set_column("J:J", 27)
worksheet.set_column("K:K", 28)

# green_format = workbook.add_format({'bg_color': '#7FFAC0', 'font_color':'#000000'})
# red_format = workbook.add_format({'bg_color': '#FA7F7F', 'font_color':'#000000'})

# worksheet.conditional_format('K2:K50', {'type':'cell', 'criteria': 'between','minimum':5,'maximum':12, 'format': green_format})
# worksheet.conditional_format('K2:K50', {'type':'cell', 'criteria': 'not between', 'minimum':5, 'maximum':12, 'format': red_format})


writer.save()

print("Excel workbook 'ShipmentPrediction' created.")