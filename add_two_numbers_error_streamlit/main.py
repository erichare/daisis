import streamlit as st
import os

print(os.environ)

def compute(firstNumber: float=4, secondNumber: float=5):
    # Compute the add
    result = firstNumber + secondNumber
    print(os.environ)

    return os.environ

st.title('Add Two Numbers!')
st.text(compute(5, 6))
