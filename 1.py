# Если выписать все натуральные числа меньше 10, 
# кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

max_n = 1000


def sumArray(array):
    sum = 0
    for element in array:
        sum += element
    return sum


def generate_array(n):
    array = []
    for i in range(1, n + 1):
        array.append(i)
    return array


def multiplicity(target_array, divider):
    dividers_array = []
    for i in target_array:
        if i % divider == 0:
            dividers_array.append(i)
    return dividers_array


def sum_all_elements(array):
    sum = 0
    for i in array:
        sum += i
    return sum


if __name__ == '__main__':
    array = multiplicity(generate_array(max_n - 1), 3) + multiplicity(generate_array(max_n - 1), 5)
    print(sum_all_elements(array))
