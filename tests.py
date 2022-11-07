def stringofication(input):
    value, name = input[0], input[1]
    if value != '0':
        string = str(value)+' '+name+'s' if value > 1 else str(value)+' '+name
        return string


print(stringofication([22, 'second']))
print(stringofication([1, 'minute']))