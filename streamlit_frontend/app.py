import streamlit as st
import pandas as pd
import requests
import json


## Basic config start ##

st.set_page_config(
    page_title ="Data Jobs", 
    layout="wide", 
    page_icon="💿",
    initial_sidebar_state="expanded",
    menu_items = {
        'Get Help': None,
        'Report a bug': None,
        'About': 'Web app by Ray Lu, Inspired by Ray Chen.'
    }
)

hide_streamlit_footer = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_footer, unsafe_allow_html=True) 

botton_color = st.markdown("""
        <style>
        div.stButton > button:first-child {
                        background-color:#002A6B  ;
                        width: 625px;
                        height: 50px;
                        font-size: 30px;
                        font-weight: bold;
                        border: 4px solid rgba(255, 147, 0, 0.2);
                        }

        </style>""", unsafe_allow_html=True)
## Basic config end ##

### only check if there're any empty in all boxes
def check_empty(values:list):
    
    if ("" in values or 0 in values):    
        st.error(f"{'All the boxes are required! Please select a value.'}")
        st.stop()
    else:
        pass






def main():

    ## Layout config
    st.title("Data Jobs")
    activities = ["Job Type Recommend","Currently Opening Job Recommend for You","About this AI application",]#"Persional Report"
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("",activities)
    
    
    ## Job Type Recommend
    if choice == "Job Type Recommend":
      
        
        st.header("Recommend the suitable Data Related Job Type For You")
        st.write("This application enables to classify the suitable Data Related Job Type according to your Ability and Expectation.")
        

        #check the problem here maybe???
        if st.session_state == {}:
            st.session_state = {
                                "Min_Salary":0,
                                "Max_Salary":0,
                                "FAANG":"",
                                "Senior":"",
                                "New_company":"",
                                "Java":"",
                                "R":"",
                                "SQL":"",
                                "Python":"",
                                "Database":"",
                                "ETL":"",
                                "OOP":"" , 
                                "Modeling":"",
                                "ML":"",
                                "Tableau":"",
                                "Power_BI":"",
                                "MS":"",
                                "PHD":""
                                }
        else:
            pass

        col1, col2, col3, col4 = st.columns(4)

        Min_Salary = col1.number_input('Enter your expected minimum salary',  step = 10000, help = "IN USD$", value= st.session_state['Min_Salary'])
        Max_Salary = col2.number_input('Enter your expected maximum salary',  step = 10000, help = "IN USD$", value= st.session_state['Max_Salary'])

        FAANG = col3.selectbox("Want to find a FAANG Job?",[st.session_state['FAANG'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Senior = col4.selectbox("Want to find a Senior Job?",[st.session_state['Senior'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)            
        New_company = col1.selectbox("Want to work at Young Company?",[st.session_state['New_company'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Java = col2.selectbox("Programming Skill : Java",[st.session_state['Java'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        R = col3.selectbox("Programming Skill : R",[st.session_state['R'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        SQL = col4.selectbox("Programming Skill : SQL",[st.session_state['SQL'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Python = col1.selectbox("Programming Skill : Python",[st.session_state['Python'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Database = col2.selectbox("Software Skill : Database related",[st.session_state['Database'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)            
        ETL = col3.selectbox("Software Skill : ETL",[st.session_state['ETL'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        OOP = col4.selectbox("Software Skill : OOP",[st.session_state['OOP'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Modeling = col1.selectbox("Software Skill : Data Modeling", [st.session_state['Modeling'],"Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        ML = col2.selectbox("Software Skill : Machine Learning",[st.session_state['ML'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Tableau = col3.selectbox("Software Skill : Tableau",[st.session_state['Tableau'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Power_BI =col4.selectbox("Software Skill : Power BI",[st.session_state['Power_BI'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        MS = col1.selectbox("Education : Master Degree",[st.session_state['MS'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        PHD = col2.selectbox("Education : PH.D.",[st.session_state['PHD'], "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        
        
        features_list = {'Min_Salary':Min_Salary, 'Max_Salary':Max_Salary, 'FAANG':FAANG, 'Senior':Senior, 'New_company':New_company, 
                        'Java':Java, 'R':R, 'SQL':SQL, 'Python':Python, 'Database':Database, 'ETL':ETL, 'OOP':OOP, 'Modeling':Modeling, 
                        'ML':ML, 'Tableau':Tableau, 'Power_BI':Power_BI, 'MS':MS, 'PHD':PHD}
        
        session_list = {'Min_Salary':Min_Salary, 'Max_Salary':Max_Salary, 'FAANG':FAANG, 'Senior':Senior, 'New_company':New_company, 
                        'Java':Java, 'R':R, 'SQL':SQL, 'Python':Python, 'Database':Database, 'ETL':ETL, 'OOP':OOP, 'Modeling':Modeling, 
                        'ML':ML, 'Tableau':Tableau, 'Power_BI':Power_BI, 'MS':MS, 'PHD':PHD}
        
        st.session_state = session_list

        check_value = list(features_list.values())
        
        
        col5, col6 = st.columns([1,1])

        if col5.button("Click Here to Find Your Job!"):
            for element in list(features_list.keys()):
                if features_list[element] == 'Yes':
                    features_list[element] = 1
                elif features_list[element] == 'No':
                    features_list[element] = 0
            
            check_empty(check_value)

            
            res = requests.post(url = 'http://127.0.0.1:8000/job_type_prediction', data = json.dumps(features_list))
            col5.subheader(f"{res.json()['Prediction']}")
    
            

        if col6.button('Reset'):
            
            st.session_state = {}
            st.experimental_rerun()
        
    if choice == "Currently Opening Job Recommend for You":

        st.header("Currently Opening Data Related Job Based on Your Requirement")
        check_empty(list(st.session_state.values()))
        
        get_data_list = {}
        value = list(st.session_state.values())
        key = list(st.session_state.keys())

        for i,j in zip(key, value):
            get_data_list[i]=j
        
        
        for element in list(get_data_list.keys()):
                if get_data_list[element] == 'Yes':
                    get_data_list[element] = 1
                elif get_data_list[element] == 'No':
                    get_data_list[element] = 0
        
        

        data = requests.post(url = 'http://127.0.0.1:8000/job_recommand', data = json.dumps(get_data_list))
        df = pd.DataFrame(data.json())
        st.table(df)
        


    

if __name__ == '__main__':

    main()
