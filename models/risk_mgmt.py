from pyextremes import EVA
import pandas as pd

def get_tail_risk(returns_series):
    # Wrap your returns in an EVA object
    model = EVA(returns_series)
    # Extract extremes using a 95th percentile threshold
    model.get_extremes(method="POT", threshold=returns_series.quantile(0.95))
    model.fit_model()
    # Return 100-day return period (extreme event)
    summary = model.get_return_value(return_period=100)
    return summary