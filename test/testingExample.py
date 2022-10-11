"""Testing files: it should look something like this. """
import pytest
import src.main as m
from datetime import date

def test_Date(input_date):
    """Testing current date here."""
    # does input == date?
    currentDate = input_date
    Today = date.today().strftime("%Y-%m-%d")
    assert currentDate == Today

def test_selected_stock(stock, expected):
    """Testing Selected stock here."""
    assert stock == expected

def test_predict():
    """Testing the prediction method within main."""
    
    START = "2015-01-01"
    Today = date.today().strftime("%Y-%m-%d")
    period = 1
    input_stock = "GOOG"

    assert m.predict(input_stock, START, Today, period) is not None

def test_download_data(input):
    """Testing plot_r_data method, to see if it is None."""
    assert m.plot_r_data(input) is not None

def text_plot_prediction(data):
    period = 1
    m.plot_prediction(data, period) is not None