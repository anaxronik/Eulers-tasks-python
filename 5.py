# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?


n_max = 20
x = n_max


def is_divide_on_range_without_remain(n, div_max = n_max):
    for i in range(1, div_max+1):
        if n % i != 0:
            return False
    return True


while True:
    print('Try num = ', x)
    if is_divide_on_range_without_remain(x):
        print('Most smallest num is ', x)
        break
    x+=1