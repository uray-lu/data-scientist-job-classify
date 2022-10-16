#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 19:06:22 2022

@author: ray
"""



import pandas as pd
import numpy as np

df_de = pd.read_csv('./data/raw/DataEngineer.csv')
df_da = pd.read_csv('./data/raw/DataAnalyst.csv', index_col=(0))
df_ba = pd.read_csv('./data/raw/BusinessAnalyst.csv')
df_ds = pd.read_csv('./data/raw/DataScientist.csv', index_col=(0)).drop('index', axis =1)

# drop meaningless columns
df_ba1 = df_ba[:3692].drop(['Unnamed: 0', 'index'], axis = 1)
df_ba1.columns = df_de.columns

#reconstruct messed up columns
df_ba2 = df_ba[3692:]
df_ba2 = df_ba2.drop(['Competitors', 'Easy Apply'], axis = 1).reset_index(drop = True)
df_ba2.columns = df_de.columns

df_ba = pd.concat([df_ba1,df_ba2])

#Add Job Type

df_de['Job Type'] = 'Data Engineer'
df_da['Job Type'] = 'Data Analyst'
df_ba['Job Type'] = 'Bussiness Analyst'
df_ds['Job Type'] = 'Data Scientist'

# combine data & make output

df_combine = pd.concat([df_de, df_da, df_ds, df_ba]).reset_index(drop = True)
df_combine.replace(['-1', -1.0], np.nan, inplace = True)
df_combine.drop(['Easy Apply', 'Competitors'], axis = 1 , inplace = True)
df_combine.to_csv('./data/analysis/combined_data.csv')
