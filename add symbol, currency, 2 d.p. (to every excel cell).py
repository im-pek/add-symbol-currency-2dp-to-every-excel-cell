import xlsxwriter

import pandas as pd

df = pd.read_excel(r"L:\My Documents\Desktop\file_name.xlsx")

df.round(2)

workbook = xlsxwriter.Workbook('L:\My Documents\Desktop\file_name.xlsx')
worksheet = workbook.add_worksheet()

money_format = workbook.add_format({'num_format': '₤#,##0.00'})

#worksheet.write('A1', '32.239', money_format)

writer = pd.ExcelWriter("L:\My Documents\Desktop\file_name.xlsx", engine='xlsxwriter')

worksheet.write('A1', df.to_string(), money_format)

df.to_excel(writer, sheet_name='Sheet1')

workbook = writer.book

#worksheet = writer.sheets['Sheet1']

#workbook.close()