def solution(number):  # 1989
    dic = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    str_number = (str(number))[::-1]
    roman_number = ''
    s=(len(str_number))-1
    for a in reversed(sorted((dic.keys()))):
        if number > a:

solution(21)
