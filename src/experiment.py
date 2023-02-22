from prophet.diagnostics import performance_metrics
import streamlit as st
from prophet import Prophet


import stock_selector

def data_testing(data):
    m = stock_selector.loading_data(data)

    # st.write(m)

    # st.plot()

    model = Prophet()
    
    # stock_selector.graphs(m)
    # st.write(m.columns)

