import re
def increment_string(strng):
    number = (re.findall(r"[0-9]+$", strng))
    if number != []:
        znumber = str(int(number[0])+1).zfill(len(number[0]))
        strng = re.sub(rf"{number}+$", '', strng)
        strng = strng+znumber
        return(strng)
    elif number == []:
        return strng+'1'
    elif strng == '':
        return '1'
        
print(increment_string('foobar10001'))
print(increment_string('foobar'))
print(increment_string('227'))
print(increment_string(''))
print(increment_string(')c]hFsL?Q33041577y7nT=G19120329w%jaJja]38276138TT,"9209878200000094567"'))
