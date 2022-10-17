#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:28:21 2022

@author: ray
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from xgboost import XGBClassifier
from colorama import Fore, init
import pickle
import logging
import os



init(autoreset = True)
logging.getLogger().setLevel(logging.INFO)




class model:
    
    def __init__(self):    
        self.root_path = os.getcwd()[:os.getcwd().find('/data-scientist-job-classify')+len('data-scientist-job-classify/')]
        data = pd.read_csv(self.root_path+'/data/analysis/analysis_data.csv').drop('Unnamed: 0', axis = 1)

        modeling_data = data[['Job Type', 'Min_Salary', 'Max_Salary','FAANG','Senior','New_company' ,'Java','R', 'SQL','Python','Database','ETL' ,'OOP','Modeling', 'ML','Tableau','Power_BI','MS' ,'PHD']]
        df_ds = modeling_data[modeling_data['Job Type'] == 'Data Scientist']
        df_de = modeling_data[modeling_data['Job Type'] == 'Data Engineer']
        df_da = modeling_data[modeling_data['Job Type'] == 'Data Analyst']
        df_ba = modeling_data[modeling_data['Job Type'] == 'Bussiness Analyst']
        
        df_ds = self.rm_outlier(df_ds, 'Min_Salary')
        df_de = self.rm_outlier(df_de, 'Min_Salary')
        df_da = self.rm_outlier(df_da, 'Min_Salary')
        df_ba = self.rm_outlier(df_ba, 'Min_Salary')

        df_ds = self.rm_outlier(df_ds, 'Max_Salary')
        df_de = self.rm_outlier(df_de, 'Max_Salary')
        df_da = self.rm_outlier(df_da, 'Max_Salary')
        df_ba = self.rm_outlier(df_ba, 'Max_Salary')


        modeling_data = pd.concat([df_ds,df_de,df_da,df_ba]).reset_index(drop = True)


        self.modeling_data = modeling_data.dropna()

        
        self.labelized_data(self.modeling_data)
        
        
    def rm_outlier(self, data, column):
    
        print ("Shape Of The Before remove Outliers: ",data.shape)
        n=1.5
        #IQR = Q3-Q1
        
        IQR = np.nanpercentile(data[column],75) - np.nanpercentile(data[column],25)
        #outlier = Q3 + n*IQR 
        data=data[data[column] < np.nanpercentile(data[column],75)+n*IQR]
        #outlier = Q1 - n*IQR 
        data=data[data[column] > np.nanpercentile(data[column],25)-n*IQR]
        
        print ("Shape Of The After remove Outliers: ",data.shape)
        
        return data

    def score(self, m, x_train, y_train, x_test, y_test, train=True):
        
        if train:
            
            pred=m.predict(x_train)
            print('Train Result:\n')
            print(f"Accuracy Score: {accuracy_score(y_train, pred)*100:.2f}%")
            print(f"Precision Score: {precision_score(y_train, pred, average = 'weighted')*100:.2f}%")
            print(f"Recall Score: {recall_score(y_train, pred, average = 'weighted')*100:.2f}%")
            print(f"F1 score: {f1_score(y_train, pred, average = 'weighted')*100:.2f}%")
            print(f"Confusion Matrix:\n {confusion_matrix(y_train, pred)}")
        elif train == False:
                
            pred=m.predict(x_test)
            print('Test Result:\n')
            print(f"Accuracy Score: {accuracy_score(y_test, pred)*100:.2f}%")
            print(f"Precision Score: {precision_score(y_test, pred, average = 'weighted')*100:.2f}%")
            print(f"Recall Score: {recall_score(y_test, pred, average = 'weighted')*100:.2f}%")
            print(f"F1 score: {f1_score(y_test, pred, average = 'weighted')*100:.2f}%")
            print(f"Confusion Matrix:\n {confusion_matrix(y_test, pred)}")
        
    def labelized_data(self, modeling_data):
        
        for i in range(len(self.modeling_data)):
            
            if self.modeling_data['Job Type'].iloc[i]=='Data Scientist':
                    
               self.modeling_data['Job Type'].iloc[i] = 0
            
            elif self.modeling_data['Job Type'].iloc[i]=='Data Engineer':
                 
               self.modeling_data['Job Type'].iloc[i] = 1
            
            elif self.modeling_data['Job Type'].iloc[i]=='Data Analyst':
                
               self.modeling_data['Job Type'].iloc[i] = 2
            
            else:
                
               self.modeling_data['Job Type'].iloc[i] = 3
            
        y =  self.modeling_data['Job Type'].astype('int')
        x =  self.modeling_data.drop('Job Type', axis =1)

        #Train-test split
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=111) 
        
        return self.x_train, self.y_train, self.x_test, self.y_test

    def tunning_parameters(self):
        
        
        n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
        max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
        max_depth.append(None)
        learning_rate=[round(float(x),2) for x in np.linspace(start=0.01, stop=0.2, num=10)]
        colsample_bytree =[round(float(x),2) for x in np.linspace(start=0.1, stop=1, num=10)]

        random_grid = {'n_estimators': n_estimators,
                       'max_depth': max_depth,
                       'learning_rate': learning_rate,
                       'colsample_bytree': colsample_bytree}
        
        
        xg = XGBClassifier(random_state=66)
        xg_random = RandomizedSearchCV(estimator = xg, param_distributions=random_grid,
                              n_iter=100, cv=3, verbose=10, random_state=66, n_jobs=-1,scoring = 'accuracy',
                              return_train_score= True)
        
        
        print('-'*20+ 'Start Tunning'+'-'*20)

        xg_random.fit(self.x_train, self.y_train)
    
        
        logging.info(f"{'Model Tunning'}{'·'*20}{Fore.GREEN}{'Pass'}")
        
        return xg_random.best_params_
    
    def optimal_modeling(self):
        
        
        parameters = self.tunning_parameters()
        
        xg_optimal = XGBClassifier(colsample_bytree= parameters['colsample_bytree'], learning_rate= parameters['learning_rate'], max_depth= parameters['max_depth'], n_estimators= parameters['n_estimators'])
        xg_optimal.fit(self.x_train, self.y_train)
        
        self.score(xg_optimal, self.x_train, self.y_train, self.x_test, self.y_test, train = False)
        
        file_name = 'xgb_optimal_model.pkl'
        try:
            pickle.dump(xg_optimal, open(self.root_path+'/model/'+file_name, "wb"))
            
            logging.info(f"{'Model saving'}{'·'*20}{Fore.GREEN}{'Pass'}")
        except:
            logging.info(f"{'Model saving'}{'·'*20}{Fore.RED}{'Error'}")
    
    
        return xg_optimal





if __name__ == '__main__':
 
    
    model().optimal_modeling()














