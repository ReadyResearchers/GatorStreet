import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import datetime
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go
from sklearn.metrics import precision_score, recall_score



import graph_data

def finding_error_rate(test_data, forecast):
    error_rate = np.mean(np.abs((test_data['Close'].values - forecast['yhat'][-len(test_data):].values) / test_data['Close'].values)) * 100
    return error_rate

@st.cache
def experiment_loading_data(symbol, start_date, end_date, test_size):
    data = yf.download(symbol, start=start_date, end=end_date)
    print(data.columns)
    # data = data.rename(columns={"Date": "ds"})
    data.reset_index(inplace=True)

    # Split data into training and testing sets
    split_index = int(len(data) * (1 - test_size))
    train_data = data[:split_index]
    test_data = data[split_index:]

    return train_data, test_data


def experiment_accuracy_and_error_rate_plot(ticker, start_date, end_date, test_size):
    # Load data
    train_data, test_data = experiment_loading_data(ticker, start_date, end_date, test_size)

    # Fit Prophet model on training data
    m = Prophet()
    m.fit(train_data[['Date', 'Close']].rename(columns={"Date": "ds", "Close": "y"}))

    # Make predictions on testing data
    future = m.make_future_dataframe(periods=len(test_data))
    forecast = m.predict(future)

    # Calculate error rate and accuracy rate
    error_rate = finding_error_rate(test_data, forecast)
    accuracy_rate = 100 - error_rate

    # Create a dataframe with date and accuracy rate
    accuracy_df = pd.DataFrame({'Date': test_data['Date'], 'Accuracy Rate': accuracy_rate})

    # Create a Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=accuracy_df['Date'], y=accuracy_df['Accuracy Rate'].tolist(), name='Accuracy Rate'))

    # Set the title and axis labels
    fig.update_layout(title=f'Accuracy Rate Over Time ({ticker})', xaxis_title='Date', yaxis_title='Accuracy Rate')

    # Display the figure
    st.plotly_chart(fig)
    
    fig_error = go.Figure()
    fig_error.add_trace(go.Scatter(x=test_data['Date'], y=[error_rate]*len(test_data), mode='lines', name='Error Rate'))
    fig_error.update_layout(title='Error Rate Over Time', xaxis_title='Date', yaxis_title='Error Rate')
    st.plotly_chart(fig_error)


def experiment_with_different_hyperparameters(ticker, start_date, end_date, test_size, n_periods, seasonality_mode):
    # Load data
    train_data, test_data = experiment_loading_data(ticker, start_date, end_date, test_size)

    # Fit Prophet model on training data
    m = Prophet(n_changepoints=50, yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True, seasonality_mode=seasonality_mode)
    m.fit(train_data[['Date', 'Close']].rename(columns={"Date": "ds", "Close": "y"}))

    # Make predictions on testing data
    future = m.make_future_dataframe(periods=n_periods)
    forecast = m.predict(future)

    # Calculate error rate and accuracy rate
    error_rate = finding_error_rate(test_data, forecast)
    accuracy_rate = 100 - error_rate

    # Plot forecast and actual values
    fig = m.plot(forecast)

    # Display error rate and accuracy rate
    st.write(f"Current Error rate: {error_rate:.2f}%")
    st.write(f"Current Accuracy rate: {accuracy_rate:.2f}%")

    # Plot accuracy rate over time
    fig_accuracy = go.Figure()
    fig_accuracy.add_trace(go.Scatter(x=test_data['Date'], y=[accuracy_rate]*len(test_data), mode='lines', name='Accuracy Rate'))
    fig_accuracy.update_layout(title='Accuracy Rate Over Time', xaxis_title='Date', yaxis_title='Accuracy Rate')
    st.plotly_chart(fig_accuracy)

    # Plot error rate over time
    fig_error = go.Figure()
    fig_error.add_trace(go.Scatter(x=test_data['Date'], y=[error_rate]*len(test_data), mode='lines', name='Error Rate'))
    fig_error.update_layout(title='Error Rate Over Time', xaxis_title='Date', yaxis_title='Error Rate')
    st.plotly_chart(fig_error)


# def experiment_precision_and_recall(ticker, start_date, end_date, test_size):
#     # Load data
#     train_data, test_data = experiment_loading_data(ticker, start_date, end_date, test_size)

#     # Fit Prophet model on training data
#     m = Prophet()
#     m.fit(train_data[['Date', 'Close']].rename(columns={"Date": "ds", "Close": "y"}))

#     # Make predictions on testing data
#     # Make predictions on testing data
#     future = m.make_future_dataframe(periods=len(test_data))
#     future.rename(columns={'ds': 'Date'}, inplace=True)
#     forecast = m.predict(future)

#     # Convert predictions to binary labels (1 for increase, 0 for decrease)
#     y_true = np.where(test_data['Close'].shift(-1) > test_data['Close'], 1, 0)
#     y_pred = np.where(forecast['yhat'].shift(-1) > test_data['Close'], 1, 0)

#     # Calculate recall and precision
#     recall = recall_score(y_true, y_pred)
#     precision = precision_score(y_true, y_pred)

#     # Plot forecast and actual values
#     fig = m.plot(forecast)

#     # Display metrics
#     st.write(f"Recall: {recall:.2f}")
#     st.write(f"Precision: {precision:.2f}")

#     # Plot metrics over time
#     fig_metrics = go.Figure()
#     fig_metrics.add_trace(go.Scatter(x=test_data['Date'], y=[recall]*len(test_data), mode='lines', name='Recall'))
#     fig_metrics.add_trace(go.Scatter(x=test_data['Date'], y=[precision]*len(test_data), mode='lines', name='Precision'))
#     fig_metrics.update_layout(title='Metrics Over Time', xaxis_title='Date', yaxis_title='Metric')
#     st.plotly_chart(fig_metrics)
