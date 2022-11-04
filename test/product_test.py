#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:10:50 2022

@author: ray
"""

import pandas as pd
import pickle
from colorama import init, Fore
import os
from product import product

 
if __name__ == '__main__':
    
    
    
    test = {'Min_Salary':90000, 'Max_Salary':125000,'FAANG':0,'Senior':0,'New_company':0 ,'Java':0,'R':1, 'SQL':1,'Python':1,'Database':1,'ETL':1 ,'OOP':1,'Modeling':1, 'ML':1,'Tableau':0,'Power_BI':0,'MS':1 ,'PHD':0}
    
    product(test).jobType_recommend()
    product(test).job_recommend()
    
