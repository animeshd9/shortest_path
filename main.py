import streamlit as st
import pandas as pd
import plotly.express as px
from test import generate_random_cites


df = pd.read_csv("data.csv")


fig = px.scatter_mapbox(df, lat="lat", lon="lng", zoom=5, hover_data=["city"], height=1000, width=1000)

fig.update_layout(mapbox_style="open-street-map")
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

user_input = st.sidebar.text_input("Enter the No. of cities which youghfgcvhfgh want to visit: ")
cities = generate_random_cites(int(user_input))

st.write("Cities to visit: ", cities)

fig = px.scatter_mapbox(df[df["city"].isin(cities)], lat="lat", lon="lng", zoom=5, hover_data=["city"], height=1000, width=1000)

st.plotly_chart(fig)