import streamlit as st

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.features import add_features

from utils.filters import apply_filters

from charts.line_chart import plot_cases_trend
from charts.bar_chart import plot_top_countries
from charts.map_chart import plot_world_map
from charts.scatter_plot import plot_vaccine_vs_cases

st.set_page_config(layout="wide")

st.title("🌍 COVID-19 Dashboard")

# Load + prepare data
df = load_data()
df = clean_data(df)
df = add_features(df)

# Filters
filtered_df = apply_filters(df)

# KPI
st.metric("Total Cases", int(filtered_df["total_cases"].max()))

# Charts
st.plotly_chart(plot_cases_trend(filtered_df), use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(plot_top_countries(filtered_df), use_container_width=True)

with col2:
    st.plotly_chart(plot_vaccine_vs_cases(filtered_df), use_container_width=True)

st.plotly_chart(plot_world_map(filtered_df), use_container_width=True)