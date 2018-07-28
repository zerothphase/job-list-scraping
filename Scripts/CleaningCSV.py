# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:32:45 2018

@author: zw91
"""

import re
import csv


# The old listings have the follow text 
# "Closing in 2 days |\n\t\t\t\t\t\t\t  \t\t\t\t\t\t\t  06-July-2018"
# Only the date "06-July-2018" is needed.

# Find all such texts
getText = re.findall("Closing\D*\d{1}\D*\d{1,2}",read)

# Remove the unwanted text
with open("job.csv",'r+', encoding='utf-8') as file:
    read = file.read()
    # Find all "Closing in 2 days |\n\t\t\t\t\t\t\t  \t\t\t\t\t\t\t  ##" and replace with ##
    getText = re.findall("Closing\D*\d{1}\D*\d{1,2}",read)      
    newread = read
    for item in getText:
        editText = re.search("\d{2}$",item)
        newread = newread.replace(item,editText[0])
        
with open("job2.csv",'w', encoding='utf-8') as file:
    file.write(newread)


