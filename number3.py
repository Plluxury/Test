import re


def roman_numerals_to_int(roman_numeral: str):
    integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    result = 0

    # строка состоит только из пробелов
    if roman_numeral.isspace():
        return None

    # в строке есть кириллица или неподходящие латинские буквы
    if bool(re.search('[а-яА-Я]', roman_numeral)) or bool(re.search('[a-zA-Z][^IXVCDML]', roman_numeral)):
        return None

    # O(n)
    for i, c in enumerate(roman_numeral):
        if i + 1 < len(roman_numeral) and integers[roman_numeral[i]] < integers[roman_numeral[i + 1]]:
            result -= integers[roman_numeral[i]]
        else:
            result += integers[roman_numeral[i]]
    return result
