import os
from tkinter import PAGES
import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd


# import files
import data_explorer




PAGES = [
    'Data Explorer',
    'Stock Selector',
    'Prediction',
    'Definition / key'
]

def run_UI():
    st.set_page_config(

        page_title="Stock App",
        initial_sidebar_state = "expanded"
    )

    st.sidebar.title("Options")
    if st.session_state.page:
        page=st.sidebar.radio('Data', PAGES, index=st.session_state.page)
    else:
        page=st.sidebar.radio('Data', PAGES, index = 1)
    
    if page == 'Data Explorer': 
        st.sidebar.write("TEST DATA TEST DATATEST DATATEST DATATEST DATATEST DATATEST DATATEST DATATEST DATATEST DATATEST DATATEST DATATEST DATATEST DATA")
        data_explorer.data()
    elif page == 'Stock Selector': 
        st.sidebar.write("TEST1")
    
    elif page == 'Prediction':
        st.sidebar.write("TEST1")

    else:
        st.sidebar.write("TEST2")

    st.title("Stock App")


if __name__ == "__main__":

    if st._is_running_with_streamlit:
        url_params = st.experimental_get_query_params()
        if 'loaded' not in st.session_state: 
            # if len(url_params.keys() == 0):
            st.experimental_set_query_params(page = 'Data Explorer')
            url_params = st.experimental_get_query_params()
            st.session_state.page = PAGES.index(url_params['page'][0])
    
    
    run_UI()