import tensorflow
import pandas as pd
import streamlit as st

def compute(firstNumber: float=4, secondNumber: float=5):
    # Compute the add
    result = firstNumber + secondNumber

    return result

st.title('Add Two Numbers!')
st.text(compute(20, 2))
