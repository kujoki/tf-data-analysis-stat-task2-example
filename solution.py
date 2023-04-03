import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mu = np.mean(x)
    std = np.std(x, ddof=1)
    t = norm.ppf(1 - (1 - p) / 2)
    lower = mu - t * std / np.sqrt(n)
    upper = mu + t * std / np.sqrt(n)
    return (lower, upper)
