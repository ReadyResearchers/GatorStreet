# to run this file use command "streamlit run run.py"
# here is the main file for my comp


#imports: 
import streamlit as st
from datetime import date

# import different files: 
import stock_selector
import key
import experiment
import predict
import graph_data

# Global variables: 

# START_DATE = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

PAGES = [ # set different tabs and pages for later use
    'Stock Selector',
    'Data Explorer',
    'Prediction',
    'Key',
    'Experiments'
]



def run():
    st.set_page_config(
        initial_sidebar_state = "expanded"
    )

    st.sidebar.title("Options")
    if st.session_state.page:
        page=st.sidebar.radio('Data', PAGES, index=st.session_state.page)
    else:
        page=st.sidebar.radio('Data', PAGES, index = 0) # when loading where you will end up
    
    if page == 'Stock Selector': 
        st.sidebar.write("This page is where users could select what stock they would like to look at. At the same time explore different types of data.")
        st.title("Stock Selector")
        ticker = stock_selector.selected_stock()
        st.write("You have selected this ",ticker, " stock")

    elif page == 'Data Explorer':
        st.sidebar.write("EHSUEHUFUFH")
        st.title("Your data")
        ticker = stock_selector.selected_stock()
        data = stock_selector.loading_data(ticker)
        graph_data.data_graphs(data)

    elif page == 'Prediction':
        st.sidebar.write("The prediction page locates the prediction feature of the code project. Please note that the project is a simulation, don't invest based on what you see in this app.")
        st.title("Prediction Time")
        ticker = stock_selector.selected_stock()
        predict.predict(ticker)

    elif page == 'Experiments':
        st.title("Experiments")
        data = stock_selector.selected_stock()
        experiment.data_testing(data)

    else:
        st.sidebar.write("This page locates all the vocab you will need to learn before you really get going with the stock market.")
        st.title("Important Stock Trading Terms")

        key.key() # working

if __name__ == "__main__":
    if st._is_running_with_streamlit:
        url_params = st.experimental_get_query_params()
        if 'loaded' not in st.session_state: 
            # if len(url_params.keys() == 0):
            st.experimental_set_query_params(page = 'Stock Selector')
            url_params = st.experimental_get_query_params()
            st.session_state.page = PAGES.index(url_params['page'][0])
    run()
