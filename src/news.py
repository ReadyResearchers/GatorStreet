import requests
import streamlit as st

def get_stock_news(stock, num_articles=4):
    api_key = "1e5f6b5431a046b286973d54ca425c7f"
    url = f"https://newsapi.org/v2/everything?q={stock}&language=en&sortBy=relevancy&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json()["articles"]
    return articles[:num_articles]