#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def HeaderFile(path, destination):
    '''
    Creates an excel file named Headers.xlsx which would contain all the headers of bhavcopy files.
    
    Input Parameters:
    
    path -> Path of the directory where all bhavcopy files are stored
    destination -> Path of the directory where Headers.xlsx will be stored (Preferably any path other than the original path).
    
    '''
    import os
    import xlrd
    import pandas as pd
    import openpyxl
    import shutil

    os.chdir(path)

    file_names = os.listdir(path)

    #  Create Excel Sheet Containing Headers

    first_row = []
    for file in file_names:
        excel_sheet = xlrd.open_workbook(file)
        sheet1 =  excel_sheet.sheet_by_index(0)
        first_row.append(sheet1.row(0))

    data = pd.DataFrame(first_row)

    datatoexcel = pd.ExcelWriter("Headers.xlsx", engine = 'xlsxwriter')

    data.to_excel(datatoexcel, sheet_name="Sheet1")

    datatoexcel.save()

    # Move the file created to destination

    shutil.move("Headers.xlsx", destination)

    # Add date column to the Headers.xlsx

    header_file = destination+"\Headers.xlsx"


    current_date =[]
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        current_date.append(f_name)

    workbook = xlrd.open_workbook(header_file)
    worksheet = workbook.sheet_by_index(0)
    rows = worksheet.nrows
    cols = worksheet.ncols


    for (cd, r) in zip(current_date, range(2,rows+1)):
        workbook = openpyxl.load_workbook(header_file)
        worksheet = workbook.active
        worksheet.cell(row = r, column = cols+1).value=cd
        workbook.save(file)

