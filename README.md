# NCDEX-Bhavcopy-Web-Scrapper
---
A simple web scrapper of [NCDEX Bhavcopy](https://www.ncdex.com/MarketData/BhavCopy.aspx) files

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

First step would be to download the Bhavcopy xls files from the NCDEX website.

We start with assingning the path to our download directory and also the path to our Chromedriver.exe to specific variables.
Also, we would want to specify our start month , day and year.


An example:
```python
download_path = r"C:\Users\Documents\Practice"
driver_path = r"C:\Users\Documents\chromedriver_win32\chromedriver.exe"
mm = 8
dd = 20
yyyy = 2019
```
Note that before the paths we add `r` to denote the path to be a _raw string_. Also, the path should be inside double quotes/ single quotes.

