# selecting different stock and companines 
# display performance aka a graph 

import streamlit as st 
import pandas as pd
from datetime import date
import yfinance as yf
from plotly import graph_objs as go


START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

@st.cache

def get_data():
    path = 'stock.csv'
    return pd.read_csv(path, low_memory=False)


def data():
    df = get_data()
    df = df.drop_duplicates(subset="Name", keep="first")

    st.title("Stock Prediction")
    st.write("###")

    stocks = df['Name']
    # stocks = ("AAPL", "NFLX", "GOOG", "MSFT", "INFY", "RPOWER.NS", "BAJFINANCE.NS", "YESBANK.NS", "RCOM.NS", "EXIDEIND.NS", "TATACHEM.NS", "TATAMOTORS.NS", "RUCHI.NS")
    selected_stock = st.selectbox("Select dataset and years for prediction", stocks)

    index = df[df["Name"]==selected_stock].index.values[0]
    symbol = df["Symbol"][index]

    n_years = st.slider("", 1, 5)
    period = n_years * 365

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data_load_state = st.text("Load data ...")
    data = load_data(symbol)
    data_load_state.text("Loading data ... Done!")

    st.write("###")

    st.subheader("Raw data")
    st.write(data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
        fig.layout.update(title_text = "Time Series Data", xaxis_rangeslider_visible = True)
        st.plotly_chart(fig)

    plot_raw_data()