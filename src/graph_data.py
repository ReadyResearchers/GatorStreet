# goal of this program is to display more graphs for the users.

import streamlit as st
from plotly import graph_objs as go 
from prophet import Prophet
from prophet.plot import plot_plotly



def data_graphs(data):
    """ Going with the tab method for better organization and look."""

    tab1, tab2, tab3, tab4= st.tabs(["  Open Price  ", "  Close Price  ", "  High  ", "  Low  "])

    with tab1: 
        graph_Open_price(data)
        st.write("This graph shows the performance of the daily opening prices of a stock over time.")
    with tab2:
        graph_Close_price(data)
        st.write("This graph shows the performance graph of the daily closing prices of a stock over time.")

    with tab3:
        graph_High(data)
        st.write("This graph shows the performance graph of the daily high prices of a stock over time.")
        
    with tab4:
        graph_Low(data)
        st.write("This graph shows the performance graph of the daily low prices of a stock over time.")
        

# line=dict(color="#ffe476") use this to change colors

def graph_Open_price(data):
    """Making a performance graph here."""
    # st.write("making graphs here")

    figure = go.Figure()
    figure.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name = 'stock open'))
    figure.layout.update(title="Opening price", xaxis_rangeslider_visible=True)
    st.plotly_chart(figure)

def graph_Close_price(data):
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name = 'stock closeing price'))
    figure.layout.update(title="Closing price", xaxis_rangeslider_visible=True)

    st.plotly_chart(figure)

def graph_High(data):
    figure = go.Figure()

    figure.add_trace(go.Scatter(x=data['Date'], y=data['High'], name = 'stock_high'))
    figure.layout.update(title="High Price", xaxis_rangeslider_visible=True)
    st.plotly_chart(figure)  

def graph_Low(data):

    figure = go.Figure()

    figure.add_trace(go.Scatter(x=data['Date'], y=data['Low'], name = 'stock_low'))
    figure.layout.update(title="Low Price", xaxis_rangeslider_visible=True)
    st.plotly_chart(figure)  
