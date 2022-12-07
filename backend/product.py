


import pandas as pd
import pickle
from colorama import init, Fore
import os




class product:
    init(autoreset=True)
    def __init__(self, input_info):
        self.input_info = input_info  
        self.input_data = pd.DataFrame([input_info])
        self.root_path = os.getcwd()[:os.getcwd().find('/data-scientist-job-classify')+len('data-scientist-job-classify/')]
        
        xgb_model_loaded = pickle.load(open('xgb_optimal_model.pkl', "rb"))
        data = pd.read_csv(self.root_path+'/data/analysis/analysis_data.csv').drop('Unnamed: 0', axis =1)
        
        self.predict = xgb_model_loaded.predict(self.input_data)
        
        if self.predict[0] == 0:
            
            data = data[data['Job Type']== 'Data Scientist']
            self.jobType = 'Data Scientist' 
        elif self.predict[0] == 1:
            
            data = data[data['Job Type']== 'Data Engineer']
            self.jobType = 'Data Engineer' 
        elif self.predict[0] == 2:
            
            data = data[data['Job Type']== 'Data Analyst']
            self.jobType = 'Data Analyst'
        elif self.predict[0] == 3:
            
            data = data[data['Job Type']== 'Bussiness Analyst'] 
            self.jobType = 'Business Analyst'
        
        self.data = data

    def jobType_recommend(self):
        
        return (f"{'According to your Excepted Salary and Ability, the Job fit you the most is: '}{self.jobType}")
      
        
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




if __name__ == '__main__':
    
    
    
    test = {'Min_Salary':90000, 'Max_Salary':125000,'FAANG':0,'Senior':0,'New_company':0 ,'Java':0,'R':1, 'SQL':1,'Python':1,'Database':1,'ETL':1 ,'OOP':1,'Modeling':1, 'ML':1,'Tableau':0,'Power_BI':0,'MS':1 ,'PHD':0}
    
    product(test).jobType_recommend()
    product(test).job_recommend()

    
