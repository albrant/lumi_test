from collections import Counter
from typing import Any, Tuple


def bigger_count_symbol(string: str) -> Tuple[str, int]:
    """Функция, которая определяет, какой символ в строке
    встречается чаще всего (без учёта регистра)

    Returns:
        Tuple: функция возвращает кортеж из двух элементов:
        буквы, которая встречается чаще всего, и количества встреч этой буквы
        Например, для строки "aaaAAAbc" результатом работы будет ('a', 6).
    """
    string = string.lower()
    counter = Counter(string)
    return counter.most_common()[0]


def root_of_number(n: int) -> int | None:
    """Функция на вход принимает единственное целое число N,
    и находит целый квадратный корень из этого числа.
    Не использует функцию sqrt() из модуля Math

    Returns:
        int|None: возвращает целый квадратный корень из числа,
    если такой существует, или None, если такого корня нет.
    """
    root = n**0.5
    if root**2 == n:
        return int(root)
    else:
        return None


def is_correct_bracket_sequence(bracket_string: str) -> Any:
    """Функция получает на вход строку, состоящую из скобок,
    и проверяет, является ли данная скобочная последовательность
    правильной (ПСП).

    Returns:
        True: если последовательность является ПСП.
        Например, (()())
        False: если последовательность не является ПСП
        Например, )())
    """
    summa = 0
    for char in bracket_string:
        if char == '(':
            summa += 1
        if char == ')':
            summa -= 1
            if summa < 0:
                return False
    return summa == 0
