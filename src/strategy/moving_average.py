import pandas as pd

class MovingAverageStrategy:
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data):
        signals = pd.DataFrame(index=data.index)
        signals['price'] = data['Close']

        # Moving averages
        signals['short_ma'] = data['Close'].rolling(self.short_window).mean()
        signals['long_ma'] = data['Close'].rolling(self.long_window).mean()

        # Generate signals (clean & correct)
        signals['signal'] = (signals['short_ma'] > signals['long_ma']).astype(int)

        # Positions (buy/sell triggers)
        signals['positions'] = signals['signal'].diff()

        # Clean NaN values
        signals.fillna(0, inplace=True)

        return signals