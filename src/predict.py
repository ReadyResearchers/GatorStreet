from prophet import Prophet
from prophet.plot import plot_plotly
import streamlit as st


import stock_selector

def predict(ticker):
    data = stock_selector.loading_data(ticker)
    
    # st.write(data)
    # df_train = data[['Date', 'Close']]
    # df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})    

    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)

    future = m.make_future_dataframe(periods=1)
    forecast = m.predict(future)

    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.subheader("Forecast Components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)