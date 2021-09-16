#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import os
import pandas as pd
import xlrd
import openpyxl
import shutil


def MergeBhavcopy(path,destination):
    '''
    Merges all the bhavcopy excel files into a single excel file Data.xlsx
    
    Input paramters:
    
    path -> Path of the directory where all bhavcopy files are stored
    destination -> Path of the directory where Data.xlsx will be stored (Preferably any path other than the original path).
    
    '''
   

    os.chdir(path)

    file_names = os.listdir(path)

    # List of Dataframes
    excels = [pd.ExcelFile(name) for name in file_names]

    frames = [x.parse(x.sheet_names[0], header=None) for x in excels]

    frames[1:] = [df[1:] for df in frames[1:]]

    combined = pd.concat(frames)

    combined.to_excel("Data.xlsx", header=False, index=True)
    
    # Move the file created to destination
    shutil.move("Data.xlsx", destination)

