


import pandas as pd
import pickle
from colorama import init, Fore
import os


init(autoreset=True)

class product:
    
    def __init__(self, input_info):
        self.input_info = input_info  
        self.input_data = pd.DataFrame([input_info])
        self.root_path = os.getcwd()[:os.getcwd().find('/data-scientist-job-classify')+len('data-scientist-job-classify/')]
        
        xgb_model_loaded = pickle.load(open(self.root_path+'/model/xgb_optimal_model.pkl', "rb"))
        data = pd.read_csv(self.root_path+'/data/analysis/analysis_data.csv').drop('Unnamed: 0', axis =1)
        
        self.predict = xgb_model_loaded.predict(self.input_data)
        
        if self.predict[0] == 0:
            
            data = data[data['Job Type']== 'Data Scientist'] 
        elif self.predict[0] == 1:
            
            data = data[data['Job Type']== 'Data Engineer'] 
        elif self.predict[0] == 2:
            
            data = data[data['Job Type']== 'Data Analyst']
        elif self.predict[0] == 3:
            
            data = data[data['Job Type']== 'Bussiness Analyst'] 

        self.data = data

    def jobType_recommend(self):
        
        if self.predict[0] == 0:
            
            print(f"{'According to your Excepted Salary and Ability, the Job fit you the most is: '}{Fore.RED}{'Data Scientist'}")
        elif self.predict[0] == 1:
            
            print(f"{'According to your Excepted Salary and Ability, the Job fit you the most is: '}{Fore.RED}{'Data Engineer'}")
        elif self.predict[0] == 2:
            
            print(f"{'According to your Excepted Salary and Ability, the Job fit you the most is: '}{Fore.RED}{'Data Analyst'}")
        elif self.predict[0] == 3:
            
            print(f"{'According to your Excepted Salary and Ability, the Job fit you the most is: '}{Fore.RED}{'Bussiness Analysis'}") 
        
        return self.predict
    
    def job_recommend(self):
        

        salary_key = list(self.input_info.keys())
        salary_value = list(self.input_info.values())
        
        inable = { key:val for key, val in self.input_info.items() if val == 0}
        inable_key = list(inable.keys())
    
    
        mask1 = (self.data[salary_key[0]] > salary_value[0])&(self.data[salary_key[1]]<salary_value[1])

        self.data = self.data[mask1]

        for i in range(len(inable_key)):
    
            self.data = self.data[self.data[inable_key[i]]==0]
    

        
        result = self.data[['Job Title', 'Job Description', 'Salary Estimate','Company Name', 'Location', 'Headquarters', 'Size',
                         'Founded', 'Type of ownership', 'Industry', 'Sector', 'Revenue']].reset_index(drop = True)
        
        return result

