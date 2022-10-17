#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:19:23 2022

@author: ray
"""

import pandas as pd
import numpy as np
import re
from colorama import init, Fore
import logging
import warnings
import os
## add inplace

class feature_engineering:    
    
    
    def __init__(self):
    
        init(autoreset = True)
        logging.getLogger().setLevel(logging.INFO)
        warnings.simplefilter('ignore')
        self.root_path = os.getcwd()[:os.getcwd().find('/data-scientist-job-classify')+len('data-scientist-job-classify/')]
        self.data = pd.read_csv(self.root_path+'/data/analysis/combined_data.csv').drop('Unnamed: 0', axis =1)
        
        
    
    def salary(self, data): 
        
        min_salary = [ ]    
        max_salary = [ ]
     
        
        try:
         
            for i in range(len(data)):
             
                try:
                 
                    single  = data['Salary Estimate'][i]   
                 
                    salaryRegex = re.compile(r'(\d*)K')
                    result = salaryRegex.findall(single)
                 
                    min_salary.append(int(result[0])*1000)
                    max_salary.append(int(result[1])*1000)
               
                except:
           
                    result = [np.nan, np.nan]
                 
                    min_salary.append(result[0])
                    max_salary.append(result[1])
            
            data['Min_Salary'] = min_salary
            data['Max_Salary'] = max_salary
               
            
            
            logging.info(f"{'Rearrang the format of Estimate Salary'}{'·'*20}{Fore.GREEN}{'Pass'}")
        except:
    
            logging.info(f"{'Rearrang the format of Estimate Salary'}{'·'*20}{Fore.RED}{'Error'}")
   
        
        return data

    def size(self, data):
        
        data['Size'] = data['Size'].str.replace('employees', '') 
        data['Size'] = data['Size'].str.replace('+', 'plus')
        data['Size'] = data['Size'].replace('Unknown', None)
        data['Size'] = data['Size'].str.replace('10000plus', '10000 to 10001')
        
        size = data['Size'].str.split("to",expand=True)
        
        try:
            if size[0] is not None:
            
                data['Min_Size'] = size[0]
                data['Max_Size'] = size[1]
        
            else:
           
                data['Min_Size'] = np.nan
                data['Max_Size'] = np.nan
            
            
            logging.info(f"{'Rearrang the format of Size'}{'·'*20}{Fore.GREEN}{'Pass'}")
        except:
            
            logging.info(f"{'Rearrang the format of Size'}{'·'*20}{Fore.RED}{'Error'}")
        
        return data
    
    def rating(self):
        
        data = self.data
        try:
            for i in range(len(data)):
            
                data['Rating'][i] = float(data['Rating'][i])
                
        
        
            logging.info(f"{'Rearrang the format of Rating'}{'·'*20}{Fore.GREEN}{'Pass'}")
        except:
            
            logging.info(f"{'Rearrang the format of Rating'}{'·'*20}{Fore.RED}{'Error'}")
        
        return data
    
    def ability(self, data):
        
        jd = data['Job Description']
        
        SQL = [ ]
        Python = [ ]
        Java = [ ]
        OOP = [ ]
        Modeling = [ ]
        ML = [ ]
        Tableau = [ ]
        Power_BI = [ ]
        R = [ ]
        ETL = [ ]
        Database = [ ]
        
        MS = [ ]
        PHD = [ ]
       
        
        try:
            for i in range(len(jd)):
            
                content = jd[i].upper()
                abilityRegex = re.compile(r'(\w*)')
                ability= abilityRegex.findall(content)
            
                ms_degreeRegex = re.compile('MS|M.S.|MASTER' )
                phd_degreeRegex = re.compile('PHD|PH.D.' )
                ms_degree = ms_degreeRegex.findall(content)
                phd_degree = phd_degreeRegex.findall(content)
            
                if 'SQL' in ability:
                    SQL.append(1)
                else:
                    SQL.append(0)
                
                if 'PYTHON' in ability:
                    Python.append(1)
                else:
                    Python.append(0)
                
                if 'R' in ability:
                    R.append(1)
                else:
                    R.append(0)
                
                if 'JAVA' in ability:
                    Java.append(1)
                else:
                    Java.append(0)
                
                if 'OOP' in ability:
                    OOP.append(1)
                elif 'OBJECT-ORIENTED' in ability:
                    OOP.append(1)
                elif 'OBJECT' in ability:
                    OOP.append(1)
                else:
                    OOP.append(0)
                
                if 'MODELING' in ability:
                    Modeling.append(1)
                else:
                    Modeling.append(0)
                    
                    
                if  'MACHINE' in ability:
                    ML.append(1)
                elif 'MACHINE LEARNING' in ability:
                    ML.append(1)
                elif 'ML' in ability:
                    ML.append(1)
                else:
                    ML.append(0)
                    
                if 'TABLEAU' in ability:
                    Tableau.append(1)
                else:
                    Tableau.append(0)
                
                if 'POWER' in ability:
                    Power_BI.append(1)
                else:
                    Power_BI.append(0)
                
                if 'ETL' in ability:
                    ETL.append(1)
                else:
                    ETL.append(0)
                
                if 'DB' in ability:  
                    Database.append(1)
                elif 'MONGODB' in ability:
                    Database.append(1)
                elif 'COUCHBASE' in ability:
                    Database.append(1)
                elif 'HADOOP' in ability:
                    Database.append(1)
                else:
                    Database.append(0)
                    
                if len(ms_degree) == 0:
                    MS.append(0)
                else:
                    MS.append(1)
                
                if len(phd_degree) == 0:
                    PHD.append(0)
                else:
                    PHD.append(1)
                    
            data['SQL'] = SQL
            data['Python'] = Python
            data['Java'] = Java
            data['Modeling'] = Modeling
            data['ML'] = ML
            data['MS'] = MS 
            data['PHD'] = PHD
            data['Tableau'] = Tableau
            data['Power_BI'] = Power_BI
            data['R'] = R
            data['ETL'] = ETL
            data['Database'] = Database
            data['OOP'] = OOP    
           
            
            logging.info(f"{'Rearrang the format of ability'}{'·'*20}{Fore.GREEN}{'Pass'}")
            
        except:
            
            logging.info(f"{'Rearrang the format of ability'}{'·'*20}{Fore.RED}{'Error'}")
            
            
        return data
      
    def company_name(self, data):
        
        company = data['Company Name']
        
        FAANG = [ ]
        
        try:
            for i in range(len(company)):
            
                company_name = str(company[i])
                companyRegex = re.compile('Facebook|Apple|Amazon|Netflex|Google')
                faang = companyRegex.findall(company_name)
                
                if len(faang) == 0:
                    
                    FAANG.append(0)
                else:
                
                    FAANG.append(1)
        
            data['FAANG'] = FAANG
            
            
            logging.info(f"{'Rearrang the format of company name'}{'·'*20}{Fore.GREEN}{'Pass'}")
        except:
            
            logging.info(f"{'Rearrang the format of company name'}{'·'*20}{Fore.RED}{'Error'}")
        
        
        return data
    

    def job_title(self, data):
        
        job_title = data['Job Title']
        

        Senior = [ ]
        
        try:
            for i in range(len(job_title)):
            
                title = job_title[i].title()
                titleRegex = re.compile(r'(\w*)')
                title_type = titleRegex.findall(title)


                if 'Senior' in title_type:
                    
                    Senior.append(1)
                else:
                    Senior.append(0)
        
            data['Senior'] = Senior
            
            
            logging.info(f"{'Rearrang the format of job title'}{'·'*20}{Fore.GREEN}{'Pass'}")
        except:
            
            logging.info(f"{'Rearrang the format of job title'}{'·'*20}{Fore.RED}{'Error'}")
        
        return data
        
    def founded(self,data):
        
        founded = data['Founded']
        
        new_company =[ ]
        
        try:
            for i in range(len(founded)):
                
                if (2022 - founded[i]) <= 10:
                    new_company.append(1)
                    
                else:
                    new_company.append(0)
            data['New_company'] = new_company
            
            logging.info(f"{'Rearrang the format of founded'}{'·'*20}{Fore.GREEN}{'Pass'}")
        
        except:
            logging.info(f"{'Rearrang the format of founded'}{'·'*20}{Fore.RED}{'Error'}")
        return data
    
    def mkoutput(self):
        
        try:
            output_data = self.rating()
            output_data = self.size(output_data)
            output_data = self.ability(output_data)
            output_data = self.salary(output_data)
            output_data = self.job_title(output_data)
            output_data = self.company_name(output_data)
            output_data = self.founded(output_data)
            
             
            output_data.to_csv(self.root_path+'/data/analysis/analysis_data.csv')
            
            logging.info(f"{'Make the output data for analysis'}{'·'*20}{Fore.GREEN}{'Pass'}")
        except:
            logging.info(f"{'Make the output data for analysis'}{'·'*20}{Fore.RED}{'Error'}")
        
        return output_data




if __name__ == '__main__':
    
    
    feature_engineering().mkoutput()





