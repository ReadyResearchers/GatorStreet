# making the prediction feature here

# imports here
import streamlit as st





# global variables here 

def predict(data):
    """ Run this method for the prediction feature. """
    n_years = st.slider("", 1, 5)
    period = n_years * 365
    df_train = data[['Date', 'Close']]
