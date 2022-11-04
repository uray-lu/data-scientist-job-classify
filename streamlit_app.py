#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 06:21:23 2022

@author: ray
"""

import streamlit as st
from backend.product import product


st.write("# Find Your Sutibale Data Related Job")

col1, col2, col3 = st.columns(3)

min_salary = col1.number_input("Enter your expect minimum salary")
max_salary = col2.number_input("Enter your expect maximum salary")
faang = col3.selectbox("Want to find a FAANG Job?",["Yes","No"])
senior = col1.selectbox("Want to find a Senior Job?",["Yes","No"])
new_company = col2.selectbox("Want to work at Young Company?",["Yes","No"])
java = col3.selectbox("Programming Skill : Java",["Yes","No"])
r = col1.selectbox("Programming Skill : R",["Yes","No"])
sql = col2.selectbox("Programming Skill : SQL",["Yes","No"])
python = col3.selectbox("Programming Skill : Python",["Yes","No"])
database = col1.selectbox("Software Skill : Database related",["Yes","No"])
etl = col2.selectbox("Software Skill : ETL",["Yes","No"])
oop = col3.selectbox("Software Skill : OOP",["Yes","No"])
modeling = col1.selectbox("Software Skill : Data Modeling",["Yes","No"])
ml = col2.selectbox("Software Skill : Machine Learning",["Yes","No"])
tableau = col3.selectbox("Software Skill : Tableau",["Yes","No"])
power_bi =col1.selectbox("Software Skill : Power BI",["Yes","No"])
ms = col2.selectbox("Education : Master Degree",["Yes","No"])
phd = col3.selectbox("Education : PH.D.",["Yes","No"])



if faang == 'Yes':
    faang = 1
else:
    faang = 0
if senior == 'Yes':
    senior = 1
else:
    senior = 0
if new_company == 'Yes':
    new_company = 1
else:
    new_company = 0
if java == 'Yes':
    java = 1
else:
    java = 0
if r == 'Yes':
    r = 1
else:
    r = 0
if sql == 'Yes':
    sql = 1
else:
    sql = 0
if python == 'Yes':
    python = 1
else:
    python = 0
if database == 'Yes':
    database = 1
else:
    database = 0
if etl == 'Yes':
    etl = 1
else:
    etl = 0    
if oop == 'Yes':
    oop = 1
else:
    oop = 0    
if modeling == 'Yes':
    modeling = 1
else:
    modeling = 0    
if ml == 'Yes':
    ml = 1
else:
    ml = 0    
if tableau == 'Yes':
    tableau = 1
else:
    tableau = 0

if power_bi == 'Yes':
    power_bi = 1
else:
    power_bi = 0

if ms == 'Yes':
    ms = 1
else:
    ms = 0
if phd == 'Yes':
    phd = 1
else:
    phd = 0    
    
    
    
    
input_dict = {'Min_Salary':min_salary, 'Max_Salary':max_salary,'FAANG':faang,'Senior':senior,'New_company':new_company ,
              'Java':java,'R':r, 'SQL':sql,'Python':python,'Database':database,'ETL':etl ,'OOP':oop,'Modeling':modeling,
              'ML':ml,'Tableau':tableau,'Power_BI':power_bi,'MS':ms ,'PHD':phd}


job_type = product(input_dict).jobType_recommend()
job = product(input_dict).job_recommend()  



if st.button('Find Job'):
    
    if job_type[0] == 0:
        
        new_title = '<p style="font-family:sans-serif; color:White; font-size: 42px;">Your Sutible Job is Data Scientist.</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        sub_title = '<p style="font-family:sans-serif; color:White; font-size: 35px;">Jobs Recommended are below</p>'
        st.markdown(sub_title, unsafe_allow_html=True)
        st.dataframe(data = job)
    elif job_type[0] == 1:
        
        new_title = '<p style="font-family:sans-serif; color:White; font-size: 42px;">Your Sutible Job is Data Engineer.</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        sub_title = '<p style="font-family:sans-serif; color:White; font-size: 35px;">Jobs Recommended are below</p>'
        st.markdown(sub_title, unsafe_allow_html=True)
        st.dataframe(data = job)
    elif job_type[0] == 2:
        
        new_title = '<p style="font-family:sans-serif; color:White; font-size: 42px;">Your Sutible Job is Data Analyst.</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        sub_title = '<p style="font-family:sans-serif; color:White; font-size: 35px;">Jobs Recommended are below</p>'
        st.markdown(sub_title, unsafe_allow_html=True)
        st.dataframe(data = job)        
    elif job_type[0] == 1:
        
        new_title = '<p style="font-family:sans-serif; color:White; font-size: 42px;">Your Sutible Job is Business Analyst.</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        sub_title = '<p style="font-family:sans-serif; color:White; font-size: 35px;">Jobs Recommended are below</p>'
        st.markdown(sub_title, unsafe_allow_html=True)
        st.dataframe(data = job)        
        


        
        
        
        
        
        
        
        
        
        
