#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:36:38 2022

@author: ray
"""
import pandas as pd
import plotly.express as px
import plotly.io as io

io.renderers.default = 'svg'



def salary_jobType(data, magntitude, plot_type):
    
    data.dropna(subset = ['Min_Salary', 'Max_Salary'], inplace = True)
    
    
    if plot_type == 'box':
    
        if magntitude == 'Min':
        
            fig = px.box(data, x = data['Job Type'], y=data['Min_Salary'], title = f"{'Box Plot of '}{magntitude}{' Salary'}")
            fig.write_image("./plot/Min_salary_Job_Type_box.png")
            fig.show()  
        elif magntitude == 'Max':
        
            fig = px.box(data, x = data['Job Type'], y=data['Max_Salary'], title = f"{'Box Plot of '}{magntitude}{' Salary'}")
            fig.write_image("./plot/Max_salary_Job_Type_box.png")
            fig.show()
        
    elif plot_type == 'hist':
        
        if magntitude == 'Min':
            
            fig = px.histogram(data, x = data["Min_Salary"], color = data["Job Type"],barmode='overlay' , title =f"{'Histogram of '}{magntitude}{' Salary'}" )
            fig.write_image("./plot/Min_Salary_Job_Type_bar.png")
            fig.show()
        elif magntitude == 'Max':
            
            fig = px.histogram(data, x = data["Max_Salary"], color = data["Job Type"],barmode='overlay' , title =f"{'Histogram of '}{magntitude}{' Salary'}" )
            fig.write_image("./plot/Max_Salary_Job_Type_bar.png")
            fig.show()
            



def founded_jobType(data, new = False):
    
    if new :
        data.dropna(subset =['Founded'], inplace = True)
        data.drop(data[data['Founded'] < 2012].index, inplace = True)
        fig = px.histogram(data, x = data["Founded"], color=data['Job Type'], barmode='overlay', title = 'Histogram of Founded' )
        fig.write_image("./plot/founded_Job_Type_bar.png")
        fig.show()
    
    elif new == False:
        
        data.dropna(subset =['Founded'], inplace = True)
        fig = px.histogram(data, x = data["Founded"], color=data['Job Type'], barmode='overlay' , title = 'Histogram of new Founded' )
        fig.write_image("./plot/founded_new_Job_Type_bar.png")
        fig.show()





def size_jobType(data, job):
    
    if job == 'Data Scientist':
        data= data[data['Job Type'] == 'Data Scientist']
    elif job == 'Data Engineer':
        data= data[data['Job Type'] == 'Data Engineer']
    elif job =='Data Analyst':
        data= data[data['Job Type'] == 'Data Analyst']
    elif job == 'Bussiness Analyst':
        data= data[data['Job Type'] == 'Bussiness Analyst']
    
    fig = px.scatter(data, x = data['Min_Salary'], y = data['Max_Size'], title = f"{'Scatter Plot of size and min salary of '}{job}")
    fig.write_image(f"{'./plot/'}{'size_and_min_salary_'}{job}{'.png'}")
    fig.show()





def langue_jobType(data, langues):
    
    if langues == 'Python':
        data= data[data['Python'] == 1]
    elif langues == 'R':
        data= data[data['R'] == 1]
    elif langues =='Java':
        data= data[data['Java'] == 1]
    elif langues == 'SQL':
        data= data[data['SQL'] == 1]
    
    
    fig = px.pie(data, values = langues, names = 'Job Type',color = 'Job Type', title = f"{'Pie chart of Job Type and '}{langues}")
    fig.write_image(f"{'./plot/'}{'Pie_chart_of_job_type_'}{langues}{'.png'}")
    fig.show()




def degree_jobType(data, degree):
    
    if degree == 'MS':
        data= data[data['MS'] == 1]
    elif degree == 'PHD':
        data= data[data['PHD'] == 1]


    fig = px.pie(data, values = degree, names = 'Job Type',color = 'Job Type', title = f"{'Pie chart of Job Type and '}{degree}")
    fig.write_image(f"{'./plot/'}{'Pie_chart_of_job_type_'}{degree}{'.png'}")
    fig.show()






def tools_jobType(data, tools):
    
    if tools == 'ML':
        data= data[data['ML'] == 1]
    elif tools == 'Modeling':
        data= data[data['Modeling'] == 1]
    elif tools =='ETL':
        data= data[data['ETL'] == 1]
    elif tools == 'Database':
        data= data[data['Database'] == 1]
    elif tools == 'OOP':
        data = data[data['OOP'] == 1]

        
    fig = px.pie(data, values = tools, names = 'Job Type',color = 'Job Type', title = f"{'Pie chart of Job Type and '}{tools}")
    fig.write_image(f"{'./plot/'}{'Pie_chart_of_job_type_'}{tools}{'.png'}")
    fig.show()    




def faang_jobType(data, Senior = True):
    
    if Senior:
        
        data= data[data['FAANG'] == 1]
        data= data[data['Senior'] == 1]
    
        fig = px.histogram(data, x = data["Job Type"], color = data['FAANG'] )
        fig.write_image("./plot/FAANG_Job_Type_senior_bar.png")
        fig.show()
    
    elif Senior == False:
        
        data= data[data['FAANG'] == 1]
        
        fig = px.histogram(data, x = data["Job Type"], color = data['FAANG'] )
        fig.write_image("./plot/FAANG_Job_Type_bar.png")
        fig.show()
        




if __name__ == '__main__':
    
    data = pd.read_csv('./data/analysis/analysis_data.csv').drop('Unnamed: 0', axis = 1)
    
    salary_jobType(data, 'Min', 'box')
    salary_jobType(data, 'Max', 'box')
    salary_jobType(data, 'Min', 'hist')
    salary_jobType(data, 'Max', 'hist')
    
    founded_jobType(data, new = False)
    founded_jobType(data, new = True)

    size_jobType(data, 'Data Scientist')
    size_jobType(data, 'Data Engineer')
    size_jobType(data, 'Data Analyst')
    size_jobType(data, 'Bussiness Analyst')
    
    langue_jobType(data, 'Java')
    langue_jobType(data, 'Python')
    langue_jobType(data, 'SQL')
    langue_jobType(data, 'R')
    
    degree_jobType(data, 'MS')
    degree_jobType(data, 'PHD')
    
    tools_jobType(data, 'ML')
    tools_jobType(data, 'Modeling')
    tools_jobType(data, 'ETL')
    tools_jobType(data, 'Database')
    tools_jobType(data, 'OOP')

    faang_jobType(data)
    faang_jobType(data, Senior= False)

