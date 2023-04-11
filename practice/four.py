roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_integer(roman_numeral):
    integer = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_numerals[roman_numeral[i]] > roman_numerals[roman_numeral[i - 1]]:
            integer += roman_numerals[roman_numeral[i]] - 2 * roman_numerals[roman_numeral[i - 1]]
        else:
            integer += roman_numerals[roman_numeral[i]]
    return integer


roman_numeral = input("Введите римскую цифру: ")
print(roman_to_integer(roman_numeral))
