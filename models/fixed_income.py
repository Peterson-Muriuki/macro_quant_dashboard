import numpy as np
import yfinance as yf
from scipy.optimize import minimize

def nelson_siegel(tau, b0, b1, b2, l1):
    # The MS model formula from Course 1/M7
    return b0 + b1*((1-np.exp(-tau/l1))/(tau/l1)) + b2*((1-np.exp(-tau/l1))/(tau/l1) - np.exp(-tau/l1))

def fit_yield_curve():
    # Fetch 3mo, 2yr, 5yr, 10yr, 30yr Treasuries
    tickers = ["^IRX", "^ZT=F", "^FVX", "^TNX", "^TYX"]
    data = yf.download(tickers, period="1d")['Close'].iloc[-1]
    maturities = np.array([0.25, 2.0, 5.0, 10.0, 30.0])
    yields = data.values / 100
    
    # Minimize sum of squared residuals
    res = minimize(lambda p: np.sum((nelson_siegel(maturities, *p) - yields)**2), [0.03, -0.02, 0.02, 1.0])
    return maturities, yields, res.x