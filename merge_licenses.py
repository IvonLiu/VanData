# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:38:55 2015

@author: Ivon Liu
"""

import pandas as pd
    
total_length = 0
business_licences = []
for i in range(1997, 2016):
    temp = pd.read_csv("data/csv/"+str(i)+"business_licences.csv", dtype={12: str}, encoding='ISO-8859-1')
    business_licences.append(temp)    

merged_licences = pd.concat(business_licences)
merged_licences.to_csv("data/output/business_licences.csv", na_rep="", index=False)

print("done")
