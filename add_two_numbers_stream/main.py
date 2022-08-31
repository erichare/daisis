import time
import streamlit as st
import os

test = os.environ

def add_test(firstNumber: float=4, secondNumber: float=5):
    # Compute the add
    print(os.environ)
    time.sleep(1)
    print("Hi")
    print(test)
    time.sleep(1)
    result = firstNumber + secondNumber

    return result

def subtract(firstNumber: float=4, secondNumber: float=5):
    # Compute the add
    result = firstNumber - secondNumber

    return result


def st_ui():
    st.set_page_config(layout = "wide")
    st.title("Test Environment Variables!")

    st.write(test)
    st.write(os.environ)

if __name__ == "__main__":
    st_ui()
