import pandas as pd
import numpy as np
import math

chat_id = 834639322 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu = -31 + math.exp(1)
    size = len(x)
    v = 0
    t1 = 0
    t = 10
    for i in range(size):
        v += x[i]*(t-mu)
        t1 += (t - mu)**2
    a = v/t1
    return a
