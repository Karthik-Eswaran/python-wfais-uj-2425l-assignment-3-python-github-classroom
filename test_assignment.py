import pytest
from stock_analyzer import StockAnalyzer

def test_daily_returns_properties():
    analyzer = StockAnalyzer("sample_stock_data.csv")
    returns = analyzer.compute_daily_returns()
    assert len(returns) == len(analyzer.close_prices) - 1
    assert abs(returns.mean() - 0.00045479467148920035) < 1e-6
    assert abs(returns.std() - 0.009447394865617983) < 1e-6

def test_moving_average_values():
    analyzer = StockAnalyzer("sample_stock_data.csv")
    ma = analyzer.compute_moving_average(window=5)
    assert len(ma) == len(analyzer.close_prices) - 4
    assert abs(ma[0] - 103.94128978083546) < 1e-6
    assert all(ma >= 0)  # prices are positive, MA should be too

def test_volatility_value():
    analyzer = StockAnalyzer("sample_stock_data.csv")
    vol = analyzer.compute_volatility()
    assert abs(vol - 0.009447394865617983) < 1e-6
