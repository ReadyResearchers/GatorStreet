import streamlit as st 
import pandas as pd
from datetime import date
import yfinance as yf
from plotly import graph_objs as go


def predict():
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)

    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    st.write("***")
    st.write("###")

    st.subheader("Forecast data")
    st.write(forecast.tail())

    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.subheader("Forecast Components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)