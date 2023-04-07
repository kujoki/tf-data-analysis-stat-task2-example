import pandas as pd
import numpy as np
from scipy.stats import t
from scipy.stats import norm


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(p, x):
    alpha = 1 - p
    n = len(x)
    Xn = max(x)
    upper = (Xn-0.032)/(alpha)**(1/n)+0.032
    lower = Xn
    return (lower, upper)

