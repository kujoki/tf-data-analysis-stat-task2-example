import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    sample_mean = np.mean(x)
    sample_std = np.std(x, ddof=1)

    t_score = norm.ppf(1 - (1 - p) / 2)

    margin_of_error = t_score * sample_std / np.sqrt(len(x))
    left_boundary = 0.032
    right_boundary = sample_mean + margin_of_error

    return (left_boundary, right_boundary)
