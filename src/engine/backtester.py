class Backtester:
    def __init__(self, data, strategy, broker):
        self.data = data
        self.strategy = strategy
        self.broker = broker

    def run(self):
        signals = self.strategy.generate_signals(self.data)
        portfolio_values = []

        for date, row in signals.iterrows():
            price = row['price']
            signal = row['positions']

            if signal == 1:
                self.broker.buy(price)
            elif signal == -1:
                self.broker.sell(price)

            portfolio_value = self.broker.get_portfolio_value(price)
            portfolio_values.append(portfolio_value)

        signals['portfolio'] = portfolio_values
        return signals