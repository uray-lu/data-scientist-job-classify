
from fastapi import FastAPI, Response
from pydantic import BaseModel
from product import product
import logging
import json

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

def parse_csv(df):
    res = df.to_json(orient="records")
    parsed = json.loads(res)
    return parsed

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn")
    logger.propagate = False
    handler = logging.handlers.RotatingFileHandler("api.log",mode="a",maxBytes = 100*1024, backupCount = 3)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    

@app.get('/')
def read_root():
	return {'statue': 'API still alive'}


@app.post("/job_type_prediction")
def return_prediction(input:User_input):
    recive = input.dict()
    prediction = product(recive).jobType_recommend()

    return {'Prediction': prediction}

@app.post("/job_recommand")
def get_data(input:User_input):
    receive = input.dict()
    data = product(receive).job_recommend()

    return parse_csv(data)
