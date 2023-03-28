# GatorStreet: The User-Friendly Machine Learning Tool for Mastering the Stock Market

## Abstraction

GatorStreet is an open-source stock prediction tool that utilizes machine learning algorithms and artificial intelligence to provide up-to-date data on different aspects of the stock market, such as trends, volatility, and historical data. Its user-friendly web application design prioritizes simplicity and accessibility, making it an excellent resource for individuals with limited financial knowledge who want to learn and explore the stock market. In addition, the tool offers a risk-free environment for users to experiment with different investment strategies and make informed decisions about their future investment options.

## Intro

Are you tired of feeling overwhelmed and confused about the stock market? Do you want to learn how to make informed investment decisions but need help knowing where to start? Look no further than GatorStreet, the revolutionary educational stock sim that utilizes the power of machine learning and artificial intelligence to provide up-to-date data and insights into the complexities of the stock market.

GatorStreet isn't just another stock simulator - it's an innovative tool that empowers individuals with limited financial knowledge to learn and understand the stock market. Unlike traditional stock simulators that replicate the stock market, GatorStreet uses machine learning algorithms to analyze past stock data to simulate the stock market.

In a world where financial literacy is increasingly essential, GatorStreet provides a unique opportunity for individuals to learn about the stock market in a risk-free environment. Whether you're a beginner looking to learn the basics or an experienced investor looking to try new strategies, GatorStreet has something to offer. 

## Installation 

what do we need to install your tool:

## Tech Detail TODO (better verison)

For this demo, I will be using `yfinance` to gather data and I will be using `pyplot` to graph my data in a form of a line graph and produce a graph. Since both `yfinance` and `pyplt` are well known libaries for graphing and gathing data from stocks websites. My goal for this demo is to produce something. For instance if I look at microsoft stocks I want to be able to see past and present data. For instance, I need to be able to answer some basic questions regarding my code and the stock. 

### Tools / libraries (TODO Delete certain libaries and tools)
 - pandas 
 - streamlit 
 - numpy 
 - yfinance
 - pyplot
 - fbprophet

How will they work within your code:


## Commands

In order to run this software you will first need to install the following: `pystan`, `streamlit`, `yfinance`, `pyplot`, and `fbprophet`.

command you will use: 

- `pip install pystan==2.19.1.1`
- `pip install yfinance`
- `pip install pyplot`
- `pip install streamlit`
- `pip install Prophet`

Note that we are installing a older version of pystan, because `Prophet` will not work with the newest version of `pystan`. 

To run the program, please use the command below
- `streamlit run src/example/main.py`

## Output

```
img
```
## Related work 
 - https://data-flair.training/blogs/stock-price-prediction-machine-learning-project-in-python/
 - https://towardsdatascience.com/predicting-future-stock-market-trends-with-python-machine-learning-2bf3f1633b3c
 - https://github.com/lussierc/StockSwingPredictor
 - https://www.dataquest.io/blog/portfolio-project-predicting-stock-prices-using-pandas-and-scikit-learn/
## Future Work 

- [x] Introduce machine learning and AI into the project
- [x] Find a way for the code to grab data by it self, and give me a list of potencial candidates
- [] increase accuracy of the program
- [X] make it easier to use
- [x] produce a live graph of current data 
- [] make it more interactive, allow the user toenter a selective stock instead of it being hard coded. 
