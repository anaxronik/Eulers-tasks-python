# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#
# Найдите сумму всех простых чисел меньше двух миллионов.


import sympy  # use library for detect simple num. need to install it

i = 2
max_num = 2000000
simple_arr = []
while True:
    if sympy.isprime(i):
        simple_arr.append(i)
        print('Find new simple number = ', i)
    elif i >= max_num:
        break
    i += 1

print(simple_arr, '\nSum = ', sum(simple_arr))
