# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:32:45 2018

@author: zw91
"""

import numpy as np
import pandas as pd
import re
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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


# =============================================================================
# Matches any decimal digit; this is equivalent to the class
# Matches any non-digit character; this is equivalent to the class [^0-9].
# Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
# Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
# Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
# Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
# =============================================================================
#    my_new_string = re.sub('[^ a-zA-Z0-9]', '', string)


df = pd.read_csv("job2.csv", sep='\s*;\s*', engine='python')

df2 = df['company'].str.replace('\t','')

jobDescription = df['job_description'].tolist()
cloudstring = str(jobDescription).replace("\\xa0","").replace("Â","")
cloud = WordCloud().generate(cloudstring)
plt.imshow(cloud)
plt.axis('off')
plt.show()
    
df3 = df.job_description.apply(''.join).str.replace('[^ a-zA-Z0-9]+', '').str.replace(' +', ' ')
df3.iloc[1]
# Replace non alphanumeric characters first with a space, then remove extra spaces
df4 = df.job_description.str.replace('[^ a-zA-Z0-9]+', ' ').str.replace(' +', ' ')
df4.iloc[1]
    