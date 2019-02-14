import openpyxl
#import os

workbook = openpyxl.load_workbook('example.xlsx')

sheet = workbook.get_sheet_by_name('Sheet1')

for i in range(1, 8):
	print(i, sheet.cell(row=i, column=2).value)



