import streamlit as st
import time

st.title('Testing Streamlit Sleep')
st.text('Sleeping for 15 seconds...')

time.sleep(15)

st.text("We're all done!")
