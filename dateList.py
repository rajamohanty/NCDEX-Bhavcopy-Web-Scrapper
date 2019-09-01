#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def dateList(mm,dd,yyyy):
    '''
    Creates a list of dates from the date given in the arguments (mm -> month, dd -> date, yy -> year; eg.) till the date today in mm-dd-yyyy format.
    Parameters:
    mm -> month (eg. 1 -> January)
    dd -> day (eg. 28)
    yyyy -> year (eg. 2018)
    '''
    from datetime import timedelta, date

    def daterange(date1, date2):
        for n in range(int ((date2 - date1).days)+1):
            yield date1 + timedelta(n)

    start_dt = date(yyyy, mm, dd)
    end_dt = date.today()

    lst = [str(dt.strftime("%m-%d-%Y")) for dt in daterange(start_dt, end_dt)]
    
    return lst

