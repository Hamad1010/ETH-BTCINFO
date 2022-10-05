import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## Eetherium Crypto Assets Information
""")

tickerSymbol = 'ETH-USD'

tickerData = yf.Ticker(tickerSymbol)

tickerData.info

st.write("""
## Bitcoin Crypto Assets Information
""")

tickerSymbol = 'BTC-USD'

tickerData = yf.Ticker(tickerSymbol)

tickerData.info
