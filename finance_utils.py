import numpy as np

def moving_average(data, window):
    return np.convolve(data, np.ones(window)/window, mode='valid')

def daily_returns(data):
    return (data[1:] - data[:-1]) / data[:-1]

def volatility(returns):
    return np.std(returns)
