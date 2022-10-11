from operator import imod
import streamlit as st
# import pandas as pd

from datetime import date # https://docs.python.org/3/library/datetime.html

import yfinance as yf # https://pypi.org/project/yfinance/

# pytest (203) 

from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go 


    # TODO, making changes to streamlit
    # testing 
    # meeting with kaph after break. 


def plot_r_data(data):

    figure = go.Figure()
    figure.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name = 'stock_open'))
    figure.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name = 'stock_close'))
    figure.layout.update(title="time series testing data", xaxis_rangeslider_visible=True)
    st.plotly_chart(figure)


def predict(selected_stock, START, Today, period):
    @st.cache 
    def loading(ticker): 
        data = yf.download(ticker, START, Today) # downloading data using yf
        # from start date to current date
        data.reset_index(inplace=True)
        return data
    
    data = loading(selected_stock)
    st.write(data.tail())

    plot_r_data(data)
    plot_prediction(data, period)

def plot_prediction(data, period):
# make an prediction model here

    data_train = data[["Date","Close"]]
    data_train = data_train.rename(columns={"Date": "ds", "Close": "y"})
    m = Prophet()
    m.fit(data_train)

    future_data = m.make_future_dataframe(periods = period) # in years

    prediction = m.predict(future_data)

    st.write('Making prediction using time series test data as input: ')

    fig1 = plot_plotly(m, prediction)    
    st.plotly_chart(fig1)
    st.write('explanation:')
    st.write('1 week: what will the stock be in 1 week')
    st.write('1 month: what will the stock be in 1 month')
    st.write('6 months: what will the stock be in 6 months')
    st.write('1 year: what will the stock be in 1 year')


def main():
    START = "2015-01-01"

    Today = date.today().strftime("%Y-%m-%d") # note its a set format, looking up year-month-date

    st.title("STOCKS app")

    stocks = ("GOOG","AAPL","DIS","GME","F","NKE")
    selected_stock = st.selectbox("Select Stock", stocks)

    # using the st.slider to design the amount of years predicted in the future.
    x_years = st.slider("Select years for " , 1, 6) # 1 - 6 years into the future
    # could use in days (most up to date)
    period = x_years * 365 # could have some math problem here 

    predict(selected_stock, START, Today, period)

main()

