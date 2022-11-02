def valid_braces(string):
    numbers_list_2 = []
    braces_dict_2 = {"{":-3, "[": -2, "(": -1, ")":1, "]": 2, "}": 3}
    for brace in string:
        numbers_list_2.append(braces_dict_2[brace])
    number_1 = 0
    while number_1 <= len(numbers_list_2)-1:
        if numbers_list_2[number_1]>0:
            return False
        else:
            number_2 = number_1+1
            while number_2 < len(numbers_list_2):
                if numbers_list_2[number_1]+numbers_list_2[number_2] == 0:    
                    del numbers_list_2[number_2]
                    del numbers_list_2[number_1]
                    if numbers_list_2 == []:
                        return True
                    else:
                        number_1 += 0
                        break
                else:
                    if number_2 >= len(numbers_list_2)-1:
                        return False
                    else:
                        number_2 += 2





print(valid_braces("((){}())")) #True
print(valid_braces("[(])")) #False