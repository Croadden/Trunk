def solution(roman):
    date = 0
    roman_letters = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
    for numbers in roman:
        if numbers in roman_letters and len(roman) == 2:
            date += roman_letters[numbers]
        else:
            date += roman_letters[numbers]
    return date


print solution('IV')
