import streamlit as st
import pandas as pd
from datetime import date # https://docs.python.org/3/library/datetime.html

import yfinance as yf # https://pypi.org/project/yfinance/

from plotly import graph_objs as go 

# streamlit run (file) 
# to run the app

START = "2017-01-01"

Today = date.today().strftime("%Y-%m-%d") # note its a set format, looking up year-month-date

st.title("STOCKS app")

stocks = ("GOOG","AAPL","ASFT","GME")
selected_stock = st.selectbox("Select Stock", stocks)

# using the st.slider to design the amount of years predicted in the future.
x_days = st.slider("Select days for prediction (working progress)" , 1, 4) # 1 - 6 days into the future
# could use in days (most up to date)
period = x_days * 365 # could have some math problem here 
# TODO using what period?
# TODO testing using (years)


# loading dataset here and graph 
# how do we save the data? like put it in memory so we don't have to redownload it again

@st.cache 
def loading(ticker): 
    data = yf.download(ticker, START, Today) # downloading data using yf
    # from start date to current date
    data.reset_index(inplace=True)
    return data

data_loaded = st.text("Loading data") # starting with this
data = loading(selected_stock)
# making yearly prediction here  :

st.subheader("raw")
st.write(data.tail())

# plotting 
def plot_r_data():
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name = 'stock_open'))
    figure.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name = 'stock_close'))
    figure.layout.update(title="time series testing data", xaxis_rangeslider_visible=True)
    st.plotly_chart(figure)
plot_r_data()