# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:32:45 2018

@author: zw91
"""

import numpy as np
import pandas as pd
import re
import csv

# Closing in 2 days |\n\t\t\t\t\t\t\t  \t\t\t\t\t\t\t  06-July-2018
getText = re.findall("Closing\D*\d{1}\D*\d{1,2}",read)




with open("job.csv",'r+', encoding='utf-8') as file:
    read = file.read()
    getText = re.findall("Closing\D*\d{1}\D*\d{1,2}",read)
    newread = read
    for item in getText:
        editText = re.search("\d{2}$",item)
        newread = newread.replace(item,editText[0])
        
with open("job2.csv",'w', encoding='utf-8') as file:
    file.write(newread)



df = pd.read_csv("job2.csv", sep=';')
    
    

    