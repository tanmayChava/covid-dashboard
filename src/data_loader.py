import pandas as pd
import streamlit as 

DATA_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    return df