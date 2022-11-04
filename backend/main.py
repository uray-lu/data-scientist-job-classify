
from fastapi import FastAPI
from pydantic import BaseModel
from product import product

class User_input(BaseModel):

    Min_Salary: float
    Max_Salary: float
    FAANG: bool
    Senior: bool
    New_company: bool 
    Java: bool
    R: bool
    SQL: bool
    Python: bool
    Database: bool
    ETL: bool 
    OOP: bool
    Modeling: bool
    ML: bool
    Tableau: bool
    Power_BI: bool
    MS: bool
    PHD: bool



app = FastAPI()


@app.post("/prediction")
def return_prediction(input:User_input):
    return input.dict() 

