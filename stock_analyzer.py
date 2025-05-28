import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from finance_utils import moving_average, daily_returns, volatility

class StockAnalyzer:
    def __init__(self, filepath):
        # TODO: convert date column (datetime- inbuilt function), and initialize attributes
        self.df = pd.read_csv(filepath)
        pass

    def compute_moving_average(self, window=5):
        # TODO: Use moving_average from finance_utils
        pass

    def compute_daily_returns(self):
        # TODO: Use daily_returns from finance_utils
        pass

    def compute_volatility(self):
        # TODO: Use volatility function on daily returns
        pass

    def plot_data(self, window=5):
        # TODO: Plot close prices and moving average
        pass
