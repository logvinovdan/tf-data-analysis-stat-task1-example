import pandas as pd
import numpy as np


chat_id = 834639322 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    errors = np.random.normal(loc=-31, scale=np.exp(1), size=x.shape)   # Генерация случайных ошибок измерения скорости
    v_mean = np.mean(x + errors)   # Средняя скорость машин за 10 секунд с учетом ошибок измерения
    v_0 = 0   # Начальная скорость машин
    t = 10   # Время ускорения
    a = (v_mean - v_0) / t   # Точечная оценка коэффициента ускорения
    return a
