import pandas as pd
import numpy as np


chat_id = 834639322 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu = - 31 - np.exp(1)   # мат ожидание ошибок измерения
    var = (np.exp(2)-2) * mu ** 2   # дисперсия ошибок измерения
    a = 10 / (x.mean()**2)   # оценка кэфа ускорения по методу моментов
    return a 
