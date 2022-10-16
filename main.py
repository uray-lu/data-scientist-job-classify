#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:10:50 2022

@author: ray
"""

import pandas as pd
import pickle



data = pd.read_csv('./data/analysis/analysis_data.csv').drop('Unnamed: 0', axis =1)
xgb_model_loaded = pickle.load(open('./model/xgb_optimal_model.pkl', "rb"))

test = {'Min_Salary':1000000, 'Max_Salary':1400000,'FAANG':0,'Senior':0,'New_company':0 ,'Java':0,'R':1, 'SQL':1,'Python':1,'Database':1,'ETL':1 ,'OOP':1,'Modeling':1, 'ML':1,'Tableau':0,'Power_BI':0,'MS':1 ,'PHD':0}
d = pd.DataFrame([test])


print(xgb_model_loaded.predict(d))

#%%

c = { key:val for key, val in test.items() if val == 0}



#%%




input_key1 = list(test.keys())
input_value1 = list(test.values())

input_key2 = list(c.keys())
input_value2 = list(c.values())





#%%
mask1 = (data[input_key1[0]] > input_value1[0])&(data[input_key1[1]]<input_value1[1])







#%%

data = data[data['Job Type'] == 'Data Scientist']


mask = ((data['Min_Salary'] > 1000000)&(data['Max_Salary']<1400000)&(data['Java'] == 0)&(data['New_company'] == 0)&(data['PHD'] == 0)&(data['Tableau'] == 0)&(data['Power_BI'] == 0)&(data['Senior'] == 0))


#%%
kk = data[mask]