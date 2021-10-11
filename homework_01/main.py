"""
Домашнее задание №1
Функции и структуры данных
"""

"""
функция, которая принимает N целых чисел,
и возвращает список квадратов этих чисел
>>> power_numbers(1, 2, 5, 7)
<<< [1, 4, 25, 49]
"""

def power_numbers(list):
    power_numbers_list = []
    for i in list:
        power_numbers_list.append(i * i)
    return power_numbers_list
print(power_numbers([1, 2, 5, 7]))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

ODD = [1, 2, 3, 4, 5, 6, 7, 8]
for num in ODD:
    if num % 2 == 0:
         print(num)

print('==================')

EVEN = [1, 2, 3, 4, 5, 6, 7, 8]
for num in EVEN:
    if num % 2 != 0:
         print(num)




