import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
  x_max = np.max(x)
  n = len(x)
  g_1 = p ** (1/n)
  g_2 = 1
  left = (x_max - 0.032)/g_2 + 0.032
  right = (x_max - 0.032)/g_1 + 0.032
  return left, right
