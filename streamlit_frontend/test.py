
import requests
import json

data = {'Min_Salary':90000, 'Max_Salary':125000,'FAANG':0,'Senior':0,'New_company':0 ,'Java':0,'R':1, 'SQL':1,'Python':1,'Database':1,'ETL':1 ,'OOP':1,'Modeling':1, 'ML':1,'Tableau':0,'Power_BI':0,'MS':1 ,'PHD':0}

res = requests.post(url = 'http://127.0.0.1:8000/job_type_prediction', data = json.dumps(data))

print(res.text)
