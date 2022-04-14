from openpyxl import load_workbook
from random import randint
 
wb = load_workbook(filename = "weeble_data_complete.xlsx")


sheet_ranges = wb['Weeble Data']

x = randint(2, 1502)


if sheet_ranges[f'A{x}'].value != None:

    z = x-1
    print(z,
    sheet_ranges[f'B{x}'].value + " -", 
    sheet_ranges[f'C{x}'].value + " -", 
    sheet_ranges[f'D{x}'].value + " -",
    sheet_ranges[f'E{x}'].value + " -",
    sheet_ranges[f'F{x}'].value + " -",
    sheet_ranges[f'G{x}'].value + " -",
    sheet_ranges[f'H{x}'].value,
    sheet_ranges[f'I{x}'].value
    )

    
    sheet_ranges[f'A{x}'].value = None
    wb.save(filename = "weeble_data_complete_test.xlsx")
else:
    print("Anime Previously Selected, Please Run Again")

# for y in range(2,1502):
# #     sheet_ranges[f'A{y}'] = y-1
    
    
# wb.save(filename = "weeble_data_complete_test.xlsx")


