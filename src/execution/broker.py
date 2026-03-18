class Broker:
    def __init__(self, initial_cash=100000, transaction_cost=0.001, slippage=0.001):
        self.cash = initial_cash
        self.position = 0
        self.transaction_cost = transaction_cost
        self.slippage = slippage

    def buy(self, price):
        exec_price = price * (1 + self.slippage)
        qty = int(self.cash // exec_price)

        if qty > 0:
            total_cost = qty * exec_price * (1 + self.transaction_cost)
            self.cash -= total_cost
            self.position += qty

    def sell(self, price):
        exec_price = price * (1 - self.slippage)

        if self.position > 0:
            total_value = self.position * exec_price * (1 - self.transaction_cost)
            self.cash += total_value
            self.position = 0

    def get_portfolio_value(self, price):
        return self.cash + self.position * price