![MIT License badge](https://img.shields.io/github/license/ReadyResearchers/GatorStreet)![files](https://img.shields.io/github/directory-file-count/ReadyResearchers/GatorStreet) ![status](https://img.shields.io/github/actions/workflow/status/ReadyResearchers/GatorStreet/main.yml)
<p align="center">
  <img src="img/GatorStreet_Logo.png" />
</p>

# GatorStreet: The User-Friendly Machine Learning Tool for Mastering the Stock Market

# Table of Contents

1. [Abstract](##Abstraction)
2. [Intro](##Intro)
3. [Installation](##Installation )
4. [Output](##Output)
5. [Future_Work](## Future Work)

## Abstraction

GatorStreet is an open-source stock prediction tool that utilizes machine learning algorithms and artificial intelligence to provide up-to-date data on different aspects of the stock market, such as trends, volatility, and historical data. Its user-friendly web application design prioritizes simplicity and accessibility, making it an excellent resource for individuals with limited financial knowledge who want to learn and explore the stock market. In addition, the tool offers a risk-free environment for users to experiment with different investment strategies and make informed decisions about their future investment options.

## Intro

Are you tired of feeling overwhelmed and confused about the stock market? Do you want to learn how to make informed investment decisions but need help knowing where to start? Look no further than GatorStreet, the revolutionary educational stock sim that utilizes the power of machine learning and artificial intelligence to provide up-to-date data and insights into the complexities of the stock market.

GatorStreet isn't just another stock simulator - it's an innovative tool that empowers individuals with limited financial knowledge to learn and understand the stock market. Unlike traditional stock simulators that replicate the stock market, GatorStreet uses machine learning algorithms to analyze past stock data to simulate the stock market.

In a world where financial literacy is increasingly essential, GatorStreet provides a unique opportunity for individuals to learn about the stock market in a risk-free environment. So whether you're a beginner looking to learn the basics or an experienced investor looking to try new strategies, GatorStreet has something to offer. 

## Installation 

### Setting up a Virtual Environment
I recommend creating a virtual environment to manage dependencies. This ensures that the packages used by this project do not conflict with those of other projects.

To create a virtual environment, run the following command in your terminal:

```python -m venv <name_of_the_environment>```

To activate the virtual environment, run the following command:

```source <name_of_the_environment>/bin/activate```

To deactivate the virtual environment, simply run:

```deactivate```

### Installing Dependencies

Once you have activated your virtual environment, you can install the dependencies required for this project. To do so, run the following command:

```pip install -r requirements.txt```

### Running the Application

To run the application locally, navigate to the src directory in your terminal and run the following command:

```streamlit run main.py```

## Output

The GatorStreet application will guide you to a user-friendly web page that is designed to be easy to navigate. Here is a breakdown of the main features you can expect to see:

### Current News Page 

On the GatorStreet main page, you can use the stock selector on the sidebar to switch between different stocks and view the latest news articles related to the selected stock, as shown in the images below. The first image shows the stock selector on the sidebar, and the second image shows the latest news articles related to the selected stock.

- ![Stock](img/Select.png)

- ![Stock New](img/news.png)

### Sidebar
The sidebar contains buttons that allow you to access the different features of the application.

- ![Side Bar](img/side_bar.png)


### Data Explorer

Click the ```Data Explorer``` button on the sidebar to explore your data. This feature displays information about a stock's open/close prices, as well as the high and low price of the stock.

- ![Data Explorer](img/data.png)

### Stock Performance Prediction

To see the predicted performance of a selected stock, click the ```Prediction``` button on the sidebar. This feature displays a graph of the expected stock performance.

- ![Prediction](img/prediction.png)


### Key

The ```Key``` feature contains financial definitions that are helpful to know.

- ![Key](img/key.png)

The experiment feature locates the results of the experiment. The first experiment compares the Accuracy rate vs Error rate. 


### Experiment

The Experiment feature displays the results of two experiments.

The first experiment compares the Accuracy rate vs Error rate.

Accuracy vs Error rate (Experiment 1)

- ![Accuracy vs Error rate](img/Experiment_1.png)

The second experiment tests the model using different hyperparameters (aka different periods).

- ![Accuracy vs Error rate](img/Experiment_2.png)

### Related works:

Here are some examples of similar projects that you might find helpful for further exploration:

- Stock Price Prediction Machine Learning Project in Python by DataFlair Training: This tutorial introduces stock price prediction using machine learning techniques in Python.

- Predicting Future Stock Market Trends with Python Machine Learning by Towards Data Science: This article covers the basics of stock price prediction and demonstrates how to implement it using Python and machine learning.

- StockSwingPredictor by Lussierc: This is a Python-based project that uses machine learning techniques to predict the swings in stock prices.

- Portfolio Project: Predicting Stock Prices Using Pandas and Scikit-learn by Dataquest: This portfolio project walks through a machine learning workflow for predicting stock prices using Python libraries like pandas and scikit-learn.


## Future Work

The GatorStreet application has significant potential for further improvements and developments. One potential avenue for future work is utilizing different data sets and exploring alternate time-series forecasting models for improved forecast and future predictions. For example, incorporating diversified data could present a more comprehensive outlook of the stock market and uncover new trends not observable in the initial data set. In addition, testing different forecasting models can generate more accurate and precise predictions.

Improving the data visualization of the GatorStreet application could also enhance the user experience. While the current UX evaluation demonstrated high user satisfaction with the application, adding more interactive visualizations and detailed data could make the platform more engaging and user-friendly. Adding charts, graphs, and interactive maps to the platform could help users better understand the data.

Another potential improvement to the GatorStreet application could be the addition of more features. For instance, incorporating social media data or other external factors could enhance the platform's predictive capabilities. In addition, the application could also be upgraded to capture live data during stock market trading hours, allowing users to see real-time changes in market trends.
