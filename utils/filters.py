import streamlit as st

def apply_filters(df):
    countries = st.sidebar.multiselect(
        "Select Countries",
        options=sorted(df["location"].unique()),
        default=["India"]
    )

    min_date = df["date"].min()
    max_date = df["date"].max()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        [min_date, max_date]
    )

    filtered = df[
        (df["location"].isin(countries)) &
        (df["date"] >= str(date_range[0])) &
        (df["date"] <= str(date_range[1]))
    ]

    return filtered