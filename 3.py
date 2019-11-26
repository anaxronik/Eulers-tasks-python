# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
import random


def is_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_dividers(n):
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
            if is_simple(i):
                print('Find new simple divider for ', n, ' = ', i)
    return arr


def find_simple_dividers(arr):
    new_arr = []
    for i in arr:
        if is_simple(i):
            new_arr.append(i)
    return new_arr


if __name__ == '__main__':
    n = 600851475143
    dividers = find_dividers(n)
    simple_dividers = find_simple_dividers(dividers)
