# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
# Очевидно, что 6-ое простое число - 13.
#
# Какое число является 10001-ым простым числом?
from is_simple import is_simple

n = 10001
i = 2
simple_list = []
print(len(simple_list))
while True:
    if is_simple(i):
        simple_list.append(i)
        print('Find new simple num = ', i, '\tAmount of simple = ', len(simple_list))
    elif len(simple_list) >= n:
        print('Biggest simple number is ', simple_list[-1])
        break
    i += 1
