# GatorStreet: The User-Friendly Machine Learning Tool for Mastering the Stock Market

## Abstraction

GitRich is a user-friendly tool designed for motivated people who want to learn more about stocks. While using this tool, the user will quickly adapt and get used to how the stock market works. The GitRich tool will achieve that by using machine learning to analyze past stock data and provide the user with up-to-date data in an easy-to-digest manner.  

## Intro

How do you get rich? Some people gamble, some people just work hard. But what if I tell you that you can make money by getting into stocks. Would you have believe me? For my project, I decided to explore the combination of AI technology with the stock market. My goal is to create a tool that can predict the next big thing before it happen. I can achieve that by studying old data and current data of past stocks prices to predict the next market. 

## Implementation

TODO

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
