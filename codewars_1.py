def solution(number):  # 1989
    str_number = (str(number))[::-1]
    print(str_number)
    roman_number = ''
    s=(len(str_number))-1
    while s>=0:
        if s == 3:
            print(str_number[3])
            t = "M" * int(str_number[3])
            roman_number = roman_number+t
        if s == 2:
            print(str_number[2])
            t = "C" * int(str_number[2]) if int(str_number[2]) < 4 else ("CD" if int(str_number[2]) == 4 else ("D" + "C" * (int(str_number[2]) - 5) if int(str_number[2]) < 9 else "CM"))
            roman_number = roman_number+t
        if s == 1:
            print(str_number[1])
            t = "X" * int(str_number[1]) if int(str_number[1]) < 4 else ("XL" if int(str_number[1]) == 4 else ("L" + "X" * (int(str_number[1]) - 5) if int(str_number[1]) < 9 else "XC"))
            roman_number = roman_number + t
        if s == 0:
            print(str_number[0])
            t = "I" * int(str_number[0]) if int(str_number[0]) < 4 else ("IV" if int(str_number[0]) == 4 else ("V" + "I" * (int(str_number[0]) - 5) if int(str_number[0]) < 9 else "IX"))
            roman_number = roman_number + t
        s -= 1
        print(roman_number)
solution(21)
