# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 23:28:09 2018

@author: zw91
"""

import numpy as np
import pandas as pd
import re
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("job2.csv", sep='\s*;\s*', engine='python')

df2 = df.job_description.str.replace('[^ a-zA-Z0-9]+', ' ').str.replace(' +', ' ')
df2.iloc[1]

jobDescription = " ".join(df2.tolist())
cloud = WordCloud().generate(jobDescription)
plt.imshow(cloud)
plt.axis('off')
plt.show()