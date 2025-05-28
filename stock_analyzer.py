import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from finance_utils import moving_average, daily_returns, volatility

class StockAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df.sort_values('Date', inplace=True)
        self.df.reset_index(drop=True, inplace=True)
        self.close_prices = self.df['Close'].values
        self.volume = self.df['Volume'].values

    def compute_moving_average(self, window=5):
        return moving_average(self.close_prices, window)

    def compute_daily_returns(self):
        return daily_returns(self.close_prices)

    def compute_volatility(self):
        returns = self.compute_daily_returns()
        return volatility(returns)

    def plot_data(self, window=5):
        ma = self.compute_moving_average(window)
        plt.figure(figsize=(10, 5))
        plt.plot(self.df['Date'], self.close_prices, label='Closing Price')
        plt.plot(self.df['Date'][window-1:], ma, label=f'{window}-Day Moving Avg')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock Closing Price and Moving Average')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
