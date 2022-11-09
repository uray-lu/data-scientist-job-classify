import streamlit as st
import pandas as pd



st.set_page_config(
    page_title ="Data Jobs", 
    layout="wide", 
    page_icon="💿",
    #initial_sidebar_state="expanded",
    menu_items = {
        'Get Help': None,
        'Report a bug': None,
        'About': 'Web app by Ray Lu, Inspired by Ray Chen.'
    }
)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



#def check_empty():


def main():

    st.title("Data Jobs")
    st.header("Recommend the suitable Data Related Job Type For You")
    st.write("This application enables to classify the suitable Data Related Job Type according to your Ability and Expectation.")

    activities = ["About this AI application","Data upload and visualisation","Data preprocessing","Modeling", "Prediction"]
    st.sidebar.title("Navigation")
    st.sidebar.radio("",activities)
   
    


    #number = st.number_input('Insert a number')






    

if __name__ == '__main__':

    main()
