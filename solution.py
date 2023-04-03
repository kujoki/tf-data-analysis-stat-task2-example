import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mean = np.mean(x)
    std_error = np.std(x, ddof=1) / np.sqrt(n)
    t_score = t.ppf(1 - (1-p)/2, n-1)
    lower = mean - t_score * std_error
    upper = mean + t_score * std_error
    return (lower, upper)
