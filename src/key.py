# making the key page here

# imports here
import streamlit as st


# global variables here 

def key():
    """Making the key here."""

    tab1, tab2, tab3 = st.tabs(["__Important__", "__Some what important__", "__Good to know__"])
    # tab1, tab2, tab3 = st.columns(3)


    with tab1:
    
        st.subheader("The Stock Market")
        with st.expander("Definition"):
            st.write("The stock market is where people buy and sell shares of publicly traded companies. The term refers to all the major exchanges as a whole. The stock market allows companies to issue shares for the public to buy and sell.")
        st.subheader("Annual Report")
        with st.expander("Definition"):
            st.write("Annual reports inform shareholders about the company. It includes information like the company’s cash flow and management strategy. When you read an annual report, you’re judging the company’s solvency and financial situation.")
        st.subheader("Averaging Down")
        with st.expander("Definition"):
            st.write("refers to buying and selling the same security on different exchanges and at different price points. ")
        st.subheader("Bear Market")
        with st.expander("Definition"):
            st.write("refers to a market environment where a major index or stock falls 20% or more from its recent highs. It’s the opposite of a bull market.")

        st.subheader("Dividend")
        with st.expander("Definition"):
            st.write("A dividend is a portion of a company’s earnings paid to shareholders quarterly or annually.")
        st.subheader("Exchange")
        with st.expander("Definition"):
            st.write("A place where investors and traders buy and sell stocks.")

        st.subheader("High")
        with st.expander("Definition"):
            st.write("A high refers to a stock or index reaching a greater price point. ")
        st.subheader("Index")
        with st.expander("Definition"):
            st.write("An index is a benchmark used as a reference marker for traders and investors. ")
        st.subheader("Low")
        with st.expander("Definition"):
            st.write("Low is the opposite of high. It represents a lower price point for a stock or index.")
        st.subheader("Margin")
        with st.expander("Definition"):
            st.write("A margin account lets a trader borrow money from a broker to purchase a stock or asset. Margin is the difference between the loan amount and the securities price.")

    with tab2:
        st.subheader("Beta")
        with st.expander("Definition"):
            st.write("Beta is a measurement of a stock’s volatility compared to the overall markets.")
        st.subheader("Blue-Chip Stocks")
        with st.expander("Definition"):
            st.write("Blue-chip stocks are the stocks of large, industry-leading companies. The expression came from blue gambling chips, the highest-valued chips in casinos.")
        st.subheader("Bourse")
        with st.expander("Definition"):
            st.write("it’s another name for the stock market. It originates from a house where wealthy men gathered to trade shares. But in today’s terms, it usually refers to the Paris stock exchange or a non-U.S. stock exchange.")
        st.subheader("Bull Market")
        with st.expander("Definition"):
            st.write("A bull market is the opposite of a bear market. It refers to a market in a prolonged period of increasing stock prices at least 20% above a recent low")
        
        st.subheader("Execution")
        with st.expander("Definition"):
            st.write("When your buy or sell order completes, it’s called execution. ")
        st.subheader("Haircut")
        with st.expander("Definition"):
            st.write("It can refer to a thin spread between the market maker’s bid and ask. It can also refer to the difference between a stock’s value and the amount a bank will recognize as collateral for a loan.")

        st.subheader("Initial Public Offering (IPO)")
        with st.expander("Definition"):
            st.write("An IPO is the first sale or offering of a stock by a company to the public.")
        st.subheader("Leverage")
        with st.expander("Definition"):
            st.write("When you use leverage, you borrow capital from your broker with the goal of increasing profits. It’s one way to potentially increase gains — but it also increases losses. Don’t trade with leverage.")

    with tab3:
        st.subheader("Broker")
        with st.expander("Definition"):
            st.write("A firm or person who executes your buy and sell orders for stocks or other securities. A broker is a must for every trader.")
        st.subheader("Bid")
        with st.expander("Definition"):
            st.write("The amount of money a trader’s willing to pay per share for a stock. I")
        st.subheader("Close")
        with st.expander("Definition"):
            st.write("The time the market closes.")
        st.subheader("Day Trading")
        with st.expander("Definition"):
            st.write("Day trading is the practice of buying and selling a stock or security within the same trading day. ")
        st.subheader("Moving Average")
        with st.expander("Definition"):
            st.write("A moving average is an indicator that shows a stock’s average price per share during a specific period.")

        st.subheader("Open")
        with st.expander("Definition"):
            st.write("The start of the trading day. ")

        st.subheader("Order")
        with st.expander("Definition"):
            st.write("A trader’s bid to buy or sell a certain amount of stock.")

        st.subheader("OTC Stocks")
        with st.expander("Definition"):
            st.write("OTC stocks trade over-the-counter")

        st.subheader("Pink Sheet Stocks")
        with st.expander("Definition"):
            st.write("Pink sheet stocks are the lowest tier of OTC stocks.")

        st.subheader("Portfolio")
        with st.expander("Definition"):
            st.write("A collection of assets that makes up a trader or investor’s portfolio. ")

        st.subheader("Quote")
        with st.expander("Definition"):
            st.write("A quote is a stock’s latest trading price.")

        st.subheader("Rally")
        with st.expander("Definition"):
            st.write("A rally is a rapid increase in the general price level of the market or of the price of a stock. ")
        st.subheader("Sector")
        with st.expander("Definition"):
            st.write("A group of stocks in the same industry belong to the same sector. An example is the tech sector, which includes companies like Apple and Microsoft. ")
        st.subheader("Share Market")
        with st.expander("Definition"):
            st.write("Any market where traders can buy or sell a company’s shares.")

        