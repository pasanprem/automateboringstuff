import openpyxl
import os

wb = openpyxl.Workbook()
wb.get_sheet_names()

sheet = wb.get_sheet_by_name('Sheet')

sheet['A1'] = 42
sheet['A2'] = 'Hello'

os.chdir('C:\\Users\\pasan.premaratne\\PycharmProjects\\automateboringstuff')

wb.save('exceledit.xlsx')
sheet2 = wb.create_sheet()
wb.get_sheet_names()

sheet2.title = 'My New Sheet Name'
wb.get_sheet_names()

wb.save('exceledit2.xlsx')