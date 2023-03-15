#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for x in range(len(roman_string)):
        if x < len(roman_string) - 1 and roman_digit[roman_string[x]] < roman_digit[roman_string[x + 1]]:
            result -= roman_digit[roman_string[x]]
        else:
            result += roman_digit[roman_string[x]]
            return result
