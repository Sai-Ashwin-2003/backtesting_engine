import numpy as np

def compute_metrics(portfolio):
    returns = portfolio.pct_change().dropna()

    total_return = (portfolio.iloc[-1] / portfolio.iloc[0]) - 1

    sharpe_ratio = 0
    if returns.std() != 0:
        sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(252)

    return {
        "Total Return": round(total_return, 4),
        "Sharpe Ratio": round(sharpe_ratio, 4)
    }