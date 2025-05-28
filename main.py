from stock_analyzer import StockAnalyzer

analyzer = StockAnalyzer('sample_stock_data.csv')
analyzer.plot_data(window=10)
print("Volatility:", analyzer.compute_volatility())
