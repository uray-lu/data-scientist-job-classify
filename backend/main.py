
from fastapi import FastAPI
from pydantic import BaseModel
from product import product



class User_input(BaseModel):

    Min_Salary : float
    Max_Salary : float
    FAANG : bool
    Senior : bool
    New_company : bool 
    Java : bool
    R : bool
    SQL : bool
    Python : bool
    Database : bool
    ETL : bool 
    OOP : bool
    Modeling : bool
    ML : bool
    Tableau : bool
    Power_BI : bool
    MS : bool
    PHD : bool



app = FastAPI()

@app.get('/')
def read_root():
	return {'message': 'This is the homepage of the API '}


@app.post("/prediction")
def return_prediction(input:User_input):
    recive = input.dict()
    result = product(recive).jobType_recommend
    return result

