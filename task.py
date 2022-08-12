from colorama import Back, Fore, Style, init

from functs import (bigger_count_symbol, is_correct_bracket_sequence,
                    root_of_number)


def task1() -> None:
    print(Back.GREEN + 'Задача 1')
    print(Style.RESET_ALL)
    print(Fore.BLUE + bigger_count_symbol.__doc__ + Style.RESET_ALL)
    strings = [
        'aaaAAAbc',
        'Abracadabra',
        'Блабла'
    ]
    results = list(map(bigger_count_symbol, strings))
    answers = dict(zip(strings, results))
    for string, answer in answers.items():
        print(f'В слове {string}: "{answer[0]}" встречается {answer[1]} раз')


def task2() -> None:
    print(Back.GREEN + 'Задача 2\n' + Style.RESET_ALL)
    print(Fore.BLUE + root_of_number.__doc__ + Style.RESET_ALL)
    numbers = (25, 1, 3, 5, 100)
    results = list(map(root_of_number, numbers))
    answers = dict(zip(numbers, results))
    for number, answer in answers.items():
        print(f'√{number}={answer}')


def task3() -> None:
    print(Back.GREEN + 'Задача 3\n' + Style.RESET_ALL)
    print(Fore.BLUE + is_correct_bracket_sequence.__doc__ + Style.RESET_ALL)
    strings = [
        '(()()())',
        '((((',
        '))((',
        '((()()))'
    ]
    bools = list(map(is_correct_bracket_sequence, strings))
    answers = dict(zip(strings, bools))
    for string, is_correct in answers.items():
        answers[string] = "является ПСП" if is_correct else "не является ПСП"
        print(string, answers[string])


def main() -> None:
    """Главная функция для выполнения всех задач."""
    init()  # инициализирую функционал colorama (вывод цветного текста)
    task1()
    print()
    task2()
    print()
    task3()


if __name__ == '__main__':
    main()
