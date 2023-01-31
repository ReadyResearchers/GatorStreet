from re import L
import pytest
import run as r
import stock_selector as ss
from datetime import date


def testing_date(input_date):
    """Testing current date with the one within the method."""
    currentDate = input_date
    Today = date.today().strftime("%Y-%m-%d")
    assert currentDate == Today

def testing_stock_selector(data):
    """Testing selected stock method to see if it is none or not."""
    stock = ss.selected_stock()
    assert stock != None

def testing_graph(data):
    """Testing if graph 1 is none or not."""
    print("within test_graph")
    graph = ss.predict(data)
    assert graph != None

def testing_state_graph(data):
    """Testing if graph 1 is none or not."""
    print("within test_graph")
    state_graph = ss.state(data)
    assert state_graph != None

