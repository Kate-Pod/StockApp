import yfinance as yf #finance market data downoader from Yahoo
import streamlit as st
import pandas as pd

# Create a heading in Markdown
st.write(""" 
# Simple Stock Price App
Shown the stock **closing price** and **volume** of Google!
""")


#https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define the ticker symbol
tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period = '1d', start = '2010-5-31',
                              end = '2021-5-31')

st.write("""
## Closing Price""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price""")
st.line_chart(tickerDf.Volume)

