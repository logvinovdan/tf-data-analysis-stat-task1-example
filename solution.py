import pandas as pd
import numpy as np


chat_id = 834639322 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:   # v = v_0 + at => a = v/10
    a = x.mean()/ 10
    return a # Ваш ответ
