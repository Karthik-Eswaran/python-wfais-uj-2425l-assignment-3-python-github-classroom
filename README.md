# 📊 Assignment: Financial Data Analyzer

## Objective
Build a Python application that loads financial time series data and performs basic analysis using Object-Oriented Programming (OOP), modular design, and basic linear algebra/statistics. You will create a class to encapsulate data operations, use a separate module for computations, and produce plots using matplotlib for interpretation.

---

## Files Information
- `sample_stock_data.csv`: sample data (columns: `Date`, `Close`, `Volume`)
- `main.py`: runs everything
- `stock_analyzer.py`: the main class 
- `utils.py`: helper functions

---

## Tasks

### 1. Create the `StockAnalyzer` Class (`stock_analyzer.py`)
This class should:
- Load data from a CSV using `pandas.read_csv`.
- Convert `Date` to datetime and sort data by date.
- Store `Close` and `Volume` as NumPy arrays.

#### Required Methods
```python
class StockAnalyzer:
    def __init__(self, filepath): ...
    def compute_moving_average(self, window=5): ...
    def compute_daily_returns(self): ...
    def compute_volatility(self): ...
    def plot_data(self): ...
```

- `compute_moving_average(window)` — returns rolling average of `Close`.
- `compute_daily_returns()` — calculates daily returns:
  \[ R_t = \frac{P_t - P_{t-1}}{P_{t-1}} \]
- `compute_volatility()` — standard deviation of daily returns.
- `plot_data()` — plots `Close` and moving average with `matplotlib`.

---

### 2. Create `finance_utils.py`
Helper functions:
```python
def moving_average(data, window): ...
def daily_returns(data): ...
def volatility(returns): ...
```

These are imported by `StockAnalyzer`, not implemented inside it.

---

### 3. Write `main.py`
Example usage:
```python
from stock_analyzer import StockAnalyzer

analyzer = StockAnalyzer('sample_stock_data.csv')
analyzer.plot_data(window=10)
print("Volatility:", analyzer.compute_volatility())
```

---

## Extension Ideas (Optional)
- Compare volatility between multiple stocks.
- Flag sharp drops or spikes in price.
- Export processed results to CSV.

---

## Example Datasets

You can use real-world data from:
- [Yahoo Finance](https://finance.yahoo.com)
- [Investing.com](https://www.investing.com/)
- [Alpha Vantage](https://www.alphavantage.co)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Nasdaq Data Link](https://data.nasdaq.com)

---

Good luck and have fun analyzing your stock data!
