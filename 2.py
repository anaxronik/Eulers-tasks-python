# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. 
# Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
import numpy as np


def generate_fibonachi(max_n):
    fibo_arr = [1, 2]
    i = 0
    while True:
        i = fibo_arr[-1] + fibo_arr[-2]
        if i > max_n:
            break
        fibo_arr.append(i)

    return fibo_arr


def parity(arr):
    new_arr = []
    for i in arr:
        if i % 2 == 0:
            new_arr.append(i)
    return new_arr


if __name__ == '__main__':
    fibo = generate_fibonachi(4000000)
    parity_fibo = parity(fibo)
    sum = np.sum(parity_fibo)
    print(sum)
