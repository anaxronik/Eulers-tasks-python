# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
#
# a^2 + b^2 = c^2
# Например, 32 + 42 = 9 + 16 = 25 = 52.
#
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

max_number = 1000
sum_numbers = 1000


def find_triple_pifagor(sum_numbers):
    for a in range(1, max_number):
        for b in range(1, max_number):
            for c in range(1, max_number):
                if a < b < c and a + b + c == sum_numbers and a * a + b * b == c * c:
                    print('Find it = ', a, b, c)
                    return a * b * c


print(find_triple_pifagor(sum_numbers))
