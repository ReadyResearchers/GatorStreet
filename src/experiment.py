from prophet.diagnostics import cross_validation, performance_metrics
import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import date
from plotly import graph_objs as go 
from prophet import Prophet
from prophet.plot import plot_plotly
from prophet.plot import plot_cross_validation_metric

# breaking

import stock_selector

def experiments(ticker):
    tab1, tab2, tab3 = st.tabs(["Prediction", "Components", "Cross-validation"])
    data = stock_selector.loading_data(ticker)

    with tab1:
        st.subheader("Your Prediction")
        df_train = data[['Date', 'Close']]
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
        m = Prophet()
        m.fit(df_train)

        future = m.make_future_dataframe(periods=365)
        forecast = m.predict(future)

        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)

    with tab2:
        st.subheader("Forecast Components")
        fig2 = m.plot_components(forecast)
        st.write(fig2)

    with tab3:
        st.subheader("Cross-validation results")
        horizon = 365
        period = 180
        initial = 1095
        df_cv = cross_validation(m, initial=initial, period=period, horizon=horizon)
        df_metrics = performance_metrics(df_cv)
        st.write("Cross-validation results:")
        st.write(df_metrics)

        fig3 = plot_cross_validation_metric(df_cv, metric='mape')
        st.write(fig3)