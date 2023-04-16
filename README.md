# EDA

https://github.com/uray-lu/data-scientist-job-classify/blob/0da7f57ef1f4812850e97bc005385aca2ec6ba63/EDA.pdf



# data-scientist-job-classifier

### To Classify and Recommend the Data Related Job By the Applicant's conditions and expected Salary.


* Data is frmo kaggle and originally form Glassdoor.com
    * https://www.kaggle.com/datasets/andrewmvd/data-engineer-jobs

* venv
    * Please excute the `make install` command in the makefile
        and source the venv
    * enter `make install` in your terminal
    * enter `source venv`

* Data preprocessing `make data_manipulation`
    * All the needed script is in src, please run in the project directory.

* Features`feature_engineering`
    * Extracted From the Job Description row by Regex
    * `Max_Salary` & `Min_Salary`
    * `Company Info`
    * `Ability`
    * `Degree` 

* Model `make model_construct`
    * XGBOOST
    * The class of model is in ./model/model.py
    * including parameters tuning and model saving

* Test `make main`
    * Test the trained model


# Product

Make a simple UI by streamlit package and deploy the model on it.
* Purpose
    
    * Imforming students with more possibility in job hunting and career path.
    * Let the students who want to find a data related jobs to find out their suitable job type(Data Scientist, Data Engineer, Data Analyst, Business Analyst) by teir personal ability, degree, expected salary....
    * Recommend the position opportunity, based on the input and the model output.
    

* App `make app`
    * Create the prototype of product.
    * Local Host.


* Deploy
    * Heroku    


