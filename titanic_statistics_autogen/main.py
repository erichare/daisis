import pandas as pd
import streamlit as st

#load and process data into a global structure
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv")

def mean(field="Age"):
    return float(titanic[field].mean())

def median(field="Age"):
    return float(titanic[field].median())

def percentile(field="Age", percentile=.25):
    return float(titanic[field].quantile(float(percentile)))

def raw(rows: int=10):
    return titanic.head(int(rows))

st.write("Titanic Statistics - Updated!")

option = st.selectbox(
     'What variable would you like to use?',
     ['Age', 'Fare'])

st.write('You selected:', option)

st.metric(label="Mean", value=mean(option))
st.metric(label="Median", value=median(option))
st.dataframe(data=raw())
