import streamlit as st
import pandas as pd


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
                        
                        }

        </style>""", unsafe_allow_html=True)
## Basic config end ##

### only check if there empty on all boxes
def check_empty(values:list):
    
    if (""|0) in values:    
        st.warning(f"{'All the box required! Please select a value.'}")
        
    else:
        st.stop()

#def to_Bool(valuse:list):

#    if "yes" in valuse:


def main():

    ## Layout config
    st.title("Data Jobs")
    st.header("Recommend the suitable Data Related Job Type For You")
    st.write("This application enables to classify the suitable Data Related Job Type according to your Ability and Expectation.")

    activities = ["Job Type Recommend","Currently Opening Job Recommend","Persional Report","About this AI application"]
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("",activities)
       

    ## Job Type Recommend
    if choice == "Job Type Recommend":
        col1, col2, col3, col4 = st.columns(4)

        Min_Salary = col1.number_input('Enter your expected minimum salary',  step = 10000, help = "IN USD$" )
        Max_Salary = col2.number_input('Enter your expected maximum salary',  step = 10000, help = "IN USD$" )

        FAANG = col3.selectbox("Want to find a FAANG Job?",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Senior = col4.selectbox("Want to find a Senior Job?",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        New_company = col1.selectbox("Want to work at Young Company?",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Java = col2.selectbox("Programming Skill : Java",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        R = col3.selectbox("Programming Skill : R",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        SQL = col4.selectbox("Programming Skill : SQL",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Python = col1.selectbox("Programming Skill : Python",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Database = col2.selectbox("Software Skill : Database related",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        ETL = col3.selectbox("Software Skill : ETL",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        OOP = col4.selectbox("Software Skill : OOP",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Modeling = col1.selectbox("Software Skill : Data Modeling", ["","Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        ML = col2.selectbox("Software Skill : Machine Learning",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Tableau = col3.selectbox("Software Skill : Tableau",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        Power_BI =col4.selectbox("Software Skill : Power BI",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        MS = col1.selectbox("Education : Master Degree",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        PHD = col2.selectbox("Education : PH.D.",["", "Yes","No"], format_func=lambda x: 'Select an option' if x == "" else x)
        

        features_list = [Min_Salary, Max_Salary, FAANG, Senior, New_company, Java, R, SQL, Python, Database, ETL, OOP, 
                    Modeling, ML, Tableau, Power_BI, MS, PHD]

        if st.button("Click Here to Find Your Job!"):
            
            check_empty(features_list)


        



        

    


    






    

if __name__ == '__main__':

    main()
