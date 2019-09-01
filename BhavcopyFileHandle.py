#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def BhavcopyFileHandle(path):
    '''
    Renaming and converting all the bhavcopy files.
    
    Input Parameters:
    path -> Put in the path of the directory where all the Bhavcopy xls files are located.
    
    '''
    
    import os
    import pyexcel

    ######################################### Renaming the files from mm-dd-yyyy format to dd-mm-yyyy ############################# 

    os.chdir(path)

    print(os.getcwd())

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        f_month, f_day, f_year = f_name.split('-')
        new_name = '{}-{}-{}{}'.format(f_year, f_month, f_day, f_ext)
        os.replace(f, new_name)

    ######################################## Creating a variable old_files to contain all the paths ###################################

    str1 = path

    file_names = os.listdir(path)

    old_files = [str1 + s for s in file_names ]

    ######################################## Converting the files from xls to xlsx ################################################

    extension = '.xlsx'
    dates=[]

    for f in os.listdir():
        f_names, f_ext = os.path.splitext(f)
        dates.append(f_names)

    new_files_name = [d + extension for d in dates]

    for (old_file, new_file) in zip(old_files, new_files_name):
        pyexcel.save_as(file_name = old_file, dest_file_name = new_file)

    ######################################## Deleting the xls files ##################################################################

    dir_name = path
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".xls"):
            os.remove(os.path.join(dir_name, item))

