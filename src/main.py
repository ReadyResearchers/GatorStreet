# to run this file use command "streamlit run run.py"
# here is the main file for my comp

#imports: 
import streamlit as st
from datetime import date

# import different files: 
import design

# Global variables: 

# START_DATE = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

PAGES = [ # set different tabs and pages for later use
    'Stock News',
    'Data Explorer',
    'Prediction',
    'Key',
    'Experiments'
]


def run():
    st.set_page_config(
        initial_sidebar_state = "expanded"
    )

    st.sidebar.title("Options: ")
    if st.session_state.page:
        page=st.sidebar.radio('Features', PAGES, index=st.session_state.page)
    else:
        page=st.sidebar.radio('Features', PAGES, index = 0) # when loading where you will end up
        
    if page == 'Stock News': 
        # st.write(articles)
        design.Stock_selector_design()
    elif page == 'Data Explorer':
        design.Data_Explorer_design()
    elif page == 'Prediction':
        design.Prediction_design()
    elif page == 'Experiments':
        design.Experiment_design()
    else:
        design.Key_design() # working

if __name__ == "__main__":
    if st._is_running_with_streamlit:
        url_params = st.experimental_get_query_params()
        if 'loaded' not in st.session_state: 
            # if len(url_params.keys() == 0):
            st.experimental_set_query_params(page = 'Stock News')
            url_params = st.experimental_get_query_params()
            st.session_state.page = PAGES.index(url_params['page'][0])
    run()
