# NCDEX-Bhavcopy-Web-Scrapper
---
A simple web scrapper of [NCDEX Bhavcopy](https://www.ncdex.com/MarketData/BhavCopy.aspx) files.

## Prerequisites

1. [Jupyter Notebook](https://www.anaconda.com/distribution/)

2. Python packages required:
    1. [Selenium](https://anaconda.org/conda-forge/selenium)
    2. [time](https://anaconda.org/conda-forge/time)
    3. [os](https://anaconda.org/jmcmurray/os)
    4. [pandas](https://anaconda.org/anaconda/pandas)
    5. [pyexcel](https://anaconda.org/conda-forge/pyexcel)
    6. [shutil](https://anaconda.org/conda-forge/pytest-shutil)
    7. [xlrd](https://anaconda.org/anaconda/xlrd)
    8. [datetime](https://anaconda.org/trentonoliphant/datetime)
    9. [openpyxl](https://anaconda.org/anaconda/openpyxl)


3. Download [ChromeDriver](https://chromedriver.chromium.org/) for Selenium and put it in a specific directory.


## NCDEX Bhavcopy Files Download

First download the Bhavcopy xls files from the NCDEX website.

Start with assigning the path to our download directory and also the path to our Chromedriver.exe to specific variables.
Also, you would want to specify your starting month, day and year.


An example:
```python
download_path = r"C:/Users/Documents/Practice"
driver_path = r"C:/Users/Documents/chromedriver_win32/chromedriver.exe"
mm = 8
dd = 20
yyyy = 2019
```

Note: 
- Here we would want to replace the backward slash (`\`) in our paths with forward slash (`/`).
- Before the paths we add `r` to denote the path to be a _raw string_. Also, the path should be inside double quotes(`""`)/single quotes(`''`).
- The month, day and year should be in the numerical format.
- You can also check each function docstring for further information.

After we have assigned our variables their respective values. We would want to call the `BhavcopyDownload()` function and pass our variables in it as input parameters. 
__This function would download all the bhavcopy from the starting date mentioned till the current date and put all those files in the directory specified by you.__

```python
BhavcopyDownload(download_path,driver_path,mm,dd,yyyy)
```

## Bhavcopy file handling _(optional)_

You can skip these steps if your purpose is to only download the bhavcopy files.

### Renaming and converting the bhavcopy files

You can call the function `BhavcopyFileHandle()` to rename all the files from mm\dd\yyyy format to yyyy\mm\dd. This will help in sorting the bhavcopy files in your file explorer.
Furthermore, the files extension would change from `.xls` to `.xlsx`. This is required for further steps.

Create a variable which would contain the path to the directory containing the Bhavcopy files.
Example:
```python
files_path = r"C:/Users/Documents/Practice/"
```
Note:
- An extra forward slash (`/`) at the end of our path is necessary for further steps.

Now call the function `BhavcopyFileHandle()`.

Example:
```python
BhavcopyFileHandle(files_path)
```

### Creating a date column for each bhavcopy files

For easier recognition of the date of the trade in the respective bhavcopies, we would add a date column as the last column in each excel file representing the date of the publishing of the bhavcopy.

Since, we already have the required path stored in `files_path` variable.

You can call it inside the function `DateColumn()`.

Example:
```python
DateColumn(files_path)
```

### Creating an excel file containing the headers of all the bhavcopy files

This file would be useful for manual data cleaning after merging all the bhavcopy files.

Here you would have to only create a variable(`destination`) containing the destination path of the `Headers.xlsx` file.
The path of the bhavcopy files are already stored in `files_path` variable.
Then just call the ` HeaderFile()` function.

Example:
```python
files_path = r"C:/Users/Documents/Practice/"
destination = r"C:/Users/Documents/"
HeaderFile(files_path,destination)
```
Note:
- It is necessary that the path to the bhavcopy files and the destination of the `Headers.xlsx` file are not the same.


### Concatenating the bhavcopy files

Final step would be to concatenate all the bhavcopy excel files into one excel file `Data.xlsx`.

Again here you would want to assign the destination path of your `Data.xlsx` to a variable(`destination`) and call the the function `MergeBhavcopy()`
using the destination path and the bhavcopy files directory path as its argument.

Example:
```python
files_path = r"C:/Users/Documents/Practice/"
destination = r"C:/Users/Documents/"
MergeBhavcopy(files_path,destination)
```

Now you can clean the final dataset `Data.xlsx`.
