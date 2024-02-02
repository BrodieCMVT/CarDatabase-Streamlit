import streamlit as st
import numpy as np
import pandas as pd

st.title('Cars Database Streamlit App')

cars = pd.read_csv("cars.csv")

limit = st.slider('Record Limit', 1, 405, 405, step=1)
col1, col2 = st.columns(2)
with col1:
    car = st.text_input('Car Search:')
with col2:
    cylinders = st.number_input('Cylinder Count:', min_value=3, max_value=8, step=1)
    cylcheck = st.checkbox('Enable?')
st.subheader('Data:')
df = pd.DataFrame(cars)
if cylinders:
    if cylcheck:
        df = df[(df['Cylinders']==int(cylinders))]
        if car:
            df = df[(df['Car'].str.contains(car.lower()) | df['Car'].str.contains(car.capitalize())) & (df['Cylinders']==cylinders)]
    else:
        if car:
            df = df[(df['Car'].str.contains(car.lower()) | df['Car'].str.contains(car.title()) | df['Car'].str.contains(car))]
df = df.head(limit)
st.dataframe(df)
