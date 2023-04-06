import pandas as pd
import numpy as np
from scipy.stats import t

from scipy.stats import norm


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(p, x):
  alpha = 1 - p
  n = len(x)
  Xn = np.max(x)
  variance = ((Xn - 0.032)**2) / 12 #дисперсия равномерного
  t_val = t.ppf(1 - alpha/2, n-1)
  lower = Xn - t_val * np.sqrt(variance / (n-1))
  upper = Xn + t_val * np.sqrt(variance / (n-1))
  return (lower, upper)

