import pandas as pd
import streamlit as st
import datetime
import yfinance as yf



st.write(
    """
    # Stock Price Analyser

    Shown are the stock prices of Company

    """
    
)

ticker_symbol = st.text_input("Enter Stock Symbol", "AAPL", key = 'placeholder')

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Input the start date", datetime.date(2023, 9, 15))

with col2:
    end_date = st.date_input("Input the end date", datetime.date(2023, 10, 15))

ticker_data = yf.Ticker(ticker_symbol)
ticker_info = ticker_data.history(period="1d", start = start_date, end = end_date)

st.write(f"""
        ## {ticker_symbol}' stock price info:
""")

st.dataframe(ticker_info.tail(10))


## Showcasing line charts

col1, col2 = st.columns(2)

with col1:
    st.header("Daily Closing Prices")
    st.line_chart(ticker_info['Close'])


with col2:
    st.header("Daily Volumes")
    st.line_chart(ticker_info['Volume'])





