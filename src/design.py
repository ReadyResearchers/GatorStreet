import streamlit as st
import time
import stock_selector
import key
import experiment
import predict
import graph_data
import news
import experiment_1

# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "red", "orange"]
image_list = ["img/image1.jpg", "img/image2.jpg", "img/image3.jpg", "img/image4.jpg"] # List of image filenames

def Stock_selector_design():
        st.sidebar.write("This page is where users could select what stock they would like to look at. At the same time explore different types of data.")
        
        st.write("<p style='font-family: Arial; font-size: 50px; color:red'> Stock News </p>", unsafe_allow_html=True)           
        # st.write('<p style="font-size:26px; color:red;">Here is some red text</p>', unsafe_allow_html=True)
        # st.write(f"<p style='font-family: Arial; font-size: 30px; color:#00CBF3'> You Selected: {ticker} </p>", unsafe_allow_html=True)           
        ticker = stock_selector.selected_stock()

        st.write(f"<p style='font-family: Arial; font-size: 25px; color:red'> Trending News for <strong>{ticker}</strong> </p>", unsafe_allow_html=True)           

        col1, col2 = st.columns(2)
        articles = news.get_stock_news(ticker)

        with col1:
            st.image(image_list[0], caption=f"") 
            font_Stock_selector_col(articles, 0)
            st.write("\n\n")
            st.image(image_list[1], caption=f"") 
            font_Stock_selector_col(articles, 1)
        with col2: 
            st.image(image_list[2], caption=f"") 
            font_Stock_selector_col(articles,2)
            st.write("\n\n")
            st.image(image_list[3], caption=f"") 
            font_Stock_selector_col(articles,3)

def Data_Explorer_design():
    st.sidebar.write("The Data explorer option allows users to take a closer look at the data used for the prediction feature of the app.") 
    st.title("Your data")
    ticker = stock_selector.selected_stock()
    data = stock_selector.loading_data(ticker)
    graph_data.data_graphs(data)

def Prediction_design():
    st.sidebar.write("The prediction page locates the prediction feature of the code project. Please note that the project is a simulation, don't invest based on what you see in this app.")
    st.title("Prediction Time")
    ticker = stock_selector.selected_stock()
    predict.predict(ticker)

def Experiment_design():
    st.title("Experiments")
    data = stock_selector.selected_stock()

    start_date = "2015-01-01"
    end_date = "2022-01-01"
    test_size = .2

    tab1, tab2 = st.tabs(["   Experiment: Accuracy and Error rate plot   ", "   Experiment: Different Hyperparameters   "])

    with tab1:
        experiment_1.experiment_accuracy_and_error_rate_plot(data, start_date, end_date, test_size)
    with tab2:
        # Define default hyperparameters
        DEFAULT_N_PERIODS = 30
        # DEFAULT_SEASONALITY_MODE = 'multiplicative'

        # Define sidebar widgets
        n_periods = st.sidebar.slider('Number of periods to forecast:', 1, 365, DEFAULT_N_PERIODS)
        seasonality_mode = st.sidebar.selectbox('Seasonality mode:', ['additive', 'multiplicative'], index=1)

        experiment_1.experiment_with_different_hyperparameters(data, start_date, end_date, test_size, n_periods, seasonality_mode)

        # experiment_1.experiment_precision_and_recall(data, start_date, end_date, test_size)
    # graph_data.testing_graph(data)
    # new_experiment.experiment_error(data, start_date, end_date, test_size)
    
def Key_design():
    st.sidebar.write("This page locates all the vocab you will need to learn before you really get going with the stock market.")
    st.title("Important Stock Trading Terms")
    key.key()

def font_Stock_selector_col(articles, value):
    st.write(f"<p style='font-family: Arial; font-size: 25px; color:white'>{articles[value]['title']}</p>", unsafe_allow_html=True)           
    # st.write(f"<p style='font-family: Arial; font-size: 14px;'>{articles[value]['description']}</p>", unsafe_allow_html=True)
    st.write()

