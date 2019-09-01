#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def BhavcopyDownload(DownloadPath,DriverPath,mm,dd,yyyy):
    '''
    Web scrapes the NCDEX Bhavcopies to the directory of your choice
    
    Input Parameters:
    DownloadPath -> Put in the path where you want the bhavcopies to be downloaded to.
    DriverPath -> Put in the path of the directory where your ChromeDriver is located.
    mm -> Specify the start month
    dd -> Specify the start date
    yyyy -> Specify the start year
    
    '''
    
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    import time    
    
    chromeoptions = Options()
    
    # Setting the download directory 
    
    chromeoptions.add_experimental_option("prefs",{"download.default_directory": DownloadPath})
    
    # Telling chrome to ignore certificates
    chromeoptions.add_argument('--ignore-certificate-errors')
    
    driver=webdriver.Chrome(executable_path=DriverPath, options=chromeoptions)
    
    
    x = dateList(mm,dd,yyyy)
    
    str1 = r'https://ncdex.com/Downloads/Bhavcopy_Summary_File/doc/'
    str2 = r'.xls'
    
    urls = [str1 + s + str2 for s in x ]
    
    
    for url in urls:
        try:
            driver.get(url)
            time.sleep(0.7)
            driver.implicitly_wait(10)
        except TimeoutError :
            print(url, " Not loaded")
            print("Index number of the url is ", urls.index(url))
            print("Error on date: ", urls[url] )
            break
        else:
            continue
    
    driver.quit()

