import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    x_mean = np.mean(x)
    x_std = np.std(x, ddof=1)
    z_critical = norm.ppf(1 - alpha / 2)
    margin_error = z_critical * x_std / np.sqrt(n)

    lower = x_mean - margin_error - 0.032
    upper = x_mean + margin_error - 0.032

    return lower, upper
