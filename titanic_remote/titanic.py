from pydaisi import Daisi
import streamlit as st

@st.cache
def load_daisi():
    t = Daisi("Titanic Statistics", base_url="https://dev3.daisi.io")

    return t


t = load_daisi()

st.write("Titanic Statistics")

option = st.selectbox(
     'What variable would you like to use?',
     ['Age', 'Fare'])

st.write('You selected:', option)

st.metric(label="Mean", value=t.mean(option).value)
st.metric(label="Median", value=t.median(option).value)
st.dataframe(data=t.raw().value)
