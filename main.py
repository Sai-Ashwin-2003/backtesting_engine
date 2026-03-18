from src.data.data_loader import load_data
from src.strategy.moving_average import MovingAverageStrategy
from src.execution.broker import Broker
from src.engine.backtester import Backtester
from src.metrics.performance import compute_metrics
from src.data.yahoo_loader import load_yahoo_data

import matplotlib.pyplot as plt

def main():
    # Option 1 (local file)
    # data = load_data("data/sample_data.csv")

    # Option 2 (real data)
    data = load_yahoo_data("RELIANCE.NS")

    strategy = MovingAverageStrategy(short_window=20, long_window=50)
    broker = Broker(initial_cash=100000)

    bt = Backtester(data, strategy, broker)
    result = bt.run()

    metrics = compute_metrics(result['portfolio'])

    print("Performance Metrics:")
    print(metrics)

    # Plot equity curve
    result['portfolio'].plot(title="Equity Curve")
    plt.show()

if __name__ == "__main__":
    main()