# 📊 Assignment: Financial Data Analyzer

## Objective
Build a Python application that loads financial time series data and performs basic analysis using Object-Oriented Programming (OOP), modular design, and basic linear algebra/statistics. You will create a class to encapsulate data operations, use a separate module for computations, and produce plots for interpretation.

---

## Learning Goals
- Practice **OOP** in Python (classes, methods, attributes).
- Use **modular programming** by creating and importing your own module.
- Apply basic **statistics and linear algebra** to real-world data.
- Gain experience with **Pandas**, **NumPy**, and **Matplotlib**.

---

## Files Provided
- `sample_stock_data.csv`: sample data (columns: `Date`, `Close`, `Volume`)
- `main.py`: runs your analysis
- `stock_analyzer.py`: where your main class goes
- `finance_utils.py`: helper functions

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

## Evaluation Criteria

| Criteria                              | Points |
|--------------------------------------|--------|
| Use of classes and methods           | 30     |
| Modular structure with helper module | 20     |
| Accurate computations                | 20     |
| Readable and labeled plots           | 15     |
| Code readability and comments        | 15     |

---

## Setup
Install dependencies:
```bash
pip install pandas matplotlib numpy
```

---

## Example Datasets

You can use real-world data from:
- [Yahoo Finance](https://finance.yahoo.com)
- [Investing.com](https://www.investing.com/)
- [Alpha Vantage](https://www.alphavantage.co)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Nasdaq Data Link](https://data.nasdaq.com)

---

## ✅ Tests (for GitHub Classroom)
Place this in a `test_assignment.py` file:

```python
import pytest
from stock_analyzer import StockAnalyzer

def test_daily_returns():
    analyzer = StockAnalyzer("sample_stock_data.csv")
    returns = analyzer.compute_daily_returns()
    assert len(returns) == len(analyzer.close_prices) - 1
    assert abs(returns.mean()) < 1  # assuming simulated data is mean-reverting

def test_moving_average():
    analyzer = StockAnalyzer("sample_stock_data.csv")
    ma = analyzer.compute_moving_average(window=5)
    assert len(ma) == len(analyzer.close_prices) - 4
    assert all(ma >= 0)  # prices are positive, so MA should be too

def test_volatility():
    analyzer = StockAnalyzer("sample_stock_data.csv")
    vol = analyzer.compute_volatility()
    assert isinstance(vol, float)
    assert vol >= 0
```

---

Good luck and have fun analyzing your stock data!
