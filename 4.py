# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
#
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.


def is_palindrome(n):
    string = str(n)
    if string == string[::-1]:
        return True
    else:
        return False


n_min = 100
n_max = 999
palindrome_arr = []
for i in range(n_min,n_max+1):
    for k in range(n_min,n_max+1):
        if is_palindrome(i*k):
            palindrome_arr.append(i*k)

print('Max palindrome = ', max(palindrome_arr))

