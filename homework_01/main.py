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
        power_numbers_list.append(i**2)
    return power_numbers_list
print(power_numbers([1, 2, 5, 7]))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers():

    """
функция, которая на вход принимает список из целых чисел,
и возвращает только чётные/нечётные/простые числа
(выбор производится передачей дополнительного аргумента)

>>> filter_numbers([1, 2, 3], ODD)
<<< [1, 3]
>>> filter_numbers([2, 3, 4, 5], EVEN)
<<< [2, 4]
    """

def find_odds(numbers, odds):
    if len(numbers) == 0:
        return
    v = numbers.pop()
    if v % 2 == 1:
        odds.append(v)
    find_odds(numbers, odds)

odds = []
numbers = [1,2,3,4,5,6,7]
find_odds(numbers,odds)
# Now odds has the odd numbers
print(odds)