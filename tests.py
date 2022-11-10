value1, value2, value3 = "8923645893726583765", "9384928364923649236492379047234", ""
 
overflow = 0
for i, (number1, number2) in enumerate(zip(value1[::-1], value2[::-1])):
    overflow, result = divmod(int(number1) + int(number2) + overflow, 10)
    value3 = f"{value3}{result}"
if overflow:
    value3 = f"{overflow}{value3}"
 
print(value3)