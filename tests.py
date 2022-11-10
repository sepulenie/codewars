<<<<<<< HEAD
value1, value2, value3 = "8923645893726583765", "9384928364923649236492379047234", ""
 
overflow = 0
for i, (number1, number2) in enumerate(zip(value1[::-1], value2[::-1])):
    overflow, result = divmod(int(number1) + int(number2) + overflow, 10)
    value3 = f"{value3}{result}"
if overflow:
    value3 = f"{overflow}{value3}"
 
print(value3)
=======
def stringofication(input):
    value, name = input[0], input[1]
    if value != '0':
        string = str(value)+' '+name+'s' if value > 1 else str(value)+' '+name
        return string


print(stringofication([22, 'second']))
print(stringofication([1, 'minute']))
>>>>>>> 2375b2f06aeb4e73a79dfb81fd77d8221589b5f2
