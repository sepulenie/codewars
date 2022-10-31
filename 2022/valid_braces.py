def valid_braces(string):
    braces_dict_1 = {"{":-1, "[": -1, "(": -1, ")":1, "]": 1, "}": 1}
    braces_dict_2 = {"{":-3, "[": -2, "(": -1, ")":1, "]": 2, "}": 3}
    numbers_list_1 = []
    numbers_list_2 = []
    for brace in string:
        numbers_list_1.append(braces_dict_1[brace])
        numbers_list_2.append(braces_dict_2[brace])
    print(numbers_list_2)
    if sum(numbers_list_1) != 0:
        return False
    else:
        for number in numbers_list_2:
            brace_1 = number
            brace_2 = numbers_list_2[number+1]
            

        return True
        

          

            


print(valid_braces("{)")) #True
print(valid_braces("{)]")) #False
print(valid_braces("{}")) # True
print(valid_braces("{}()[])")) #False
print(valid_braces("(({{[[]]}}))")) #True
print(valid_braces("())({}}{()][][")) #False 