def valid_braces(string):
    numbers_list_2 = string
    print("Лист - ", numbers_list_2)
    if numbers_list_2[0]>0:
        print("Неправильный лист")
        return False
    else:    
        for number_1 in range(len(numbers_list_2)-1):
            print("Попытка №",number_1)
            brace_1 = numbers_list_2[number_1]
            for number_2 in range(number_1, numbers_list_2[number_1+i]):




valid_braces([-3, 3])
valid_braces([-3, -2, 2, 3])
#valid_braces([-3, -2, 1, 2, 3])