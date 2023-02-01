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
TODAY = date.today().strftime("%Y-%m-%d")

@st.cache
def get_data():
    print("getting stock data here")
    path = 'data/stock.csv'
    return pd.read_csv(path, low_memory=False)

# @st.cache()
def selected_stock():
    """Getting stock name here."""
    # st.title("STOCKS")
    data = get_data()
    data = data.drop_duplicates(subset="Name", keep="first")

    stocks = data['Name']

    selected_stock = st.selectbox("Select dataset and years for prediction", stocks)
    # st.write(selected_stock)

    index = data[data["Name"]==selected_stock].index.values[0]

    symbol = data["Symbol"][index]
    data_load_state = st.text("Load data ...")
    data = loading_data(symbol)
    data_load_state.text("Loading data ... Done!")

    return symbol

def graphs(data):
    """Making a performance graph here."""
    st.write("making graphs here")
    figure = go.Figure()

    figure.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name = 'stock_open'))
    figure.layout.update(title="Stock's Opening price", xaxis_rangeslider_visible=True)
    st.plotly_chart(figure)

def state(data):
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name = 'stock_close'))
    figure.layout.update(title="Stock's Closing price", xaxis_rangeslider_visible=True)

    st.plotly_chart(figure)


@st.cache
def loading_data(symbol):
    data = yf.download(symbol)
    data.reset_index(inplace=True)
    return data


# @st.cache
def predict(ticker):
    data = loading_data(ticker)
    
    # st.write(data)
    # df_train = data[['Date', 'Close']]
    # df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})    

    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)

    future = m.make_future_dataframe(periods=1)
    forecast = m.predict(future)

    # st.write("***")
    # st.write("###")

    # st.subheader("Forecast data")
    # st.write(forecast.tail())

    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.subheader("Forecast Components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)