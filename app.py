
import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(
    page_title="Country Development",
    page_icon="🌍",
    layout="centered"
)

df = pd.read_csv("Country-data.csv")
clustered_data = pd.read_csv("clustered_country_data.csv")

st.title("🌍 Country Development")

st.write("Pick a country to see its development level.")

country = st.selectbox(
    "Choose a country",
    df["country"].tolist(),
    index=None,
    placeholder="Select a country"
)

if country is not None:

    country_data = clustered_data[
        clustered_data["country"] == country
    ]

    if len(country_data) > 0:

        cluster = country_data["cluster"].iloc[0]

        development_levels = {
            0: "High Development",
            1: "Low Development",
            2: "Medium Development"
        }

        development_level = development_levels[cluster]

        if development_level == "Low Development":
            st.error(f"{country}: {development_level}")

        elif development_level == "Medium Development":
            st.warning(f"{country}: {development_level}")

        else:
            st.success(f"{country}: {development_level}")

    else:
        st.error("This country was not found in the clustered data.")

st.caption(
    "Development levels are based on the KMeans clustering "
    "results and may not represent an official classification."
)
