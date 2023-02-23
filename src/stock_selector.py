# getting stock data here.
# get data from csv file, return a stock name  

# imports: 
import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import date
from plotly import graph_objs as go 
from prophet import Prophet
from prophet.plot import plot_plotly


# global start data and today
START_DATE = "2015-01-01"
# TODAY = date.today().strftime("%Y-%m-%d")

@st.cache
def get_data():
    print("getting stock data here")
    path = 'data/stock.csv'
    return pd.read_csv(path, low_memory=False)

# @st.cache
def selected_stock():
    """Getting stock name here."""
    # st.title("STOCKS")
    data = get_data()
    data = data.drop_duplicates(subset="Name", keep="first")

    stocks = data['Name']

    selected_stock = st.selectbox("Select your dataset for", stocks)
    # st.write(selected_stock)

    index = data[data["Name"]==selected_stock].index.values[0]

    symbol = data["Symbol"][index]
    # data_load_state = st.text("Load data ...")
    data = loading_data(symbol)
    # data_load_state.text("Loading data ... Done!")

    return symbol

@st.cache
def loading_data(symbol):
    # declaring a data variable for later. 
    data = yf.download(symbol, start=START_DATE) # making the variable here.
    data.reset_index(inplace=True)
    return data # returning the data variable.
