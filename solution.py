import pandas as pd
import numpy as np

chat_id = 834639322 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = ( x - (-31 + np.exp(1))) / 10
    return x.mean() # Ваш ответ
