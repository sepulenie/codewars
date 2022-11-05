def increment_string(strng):
    strng = strng[::-1]
    if strng != '':
        for char in range(0, len(strng)):
            if strng[char].isalpha():
                word = str(strng[char:])[::-1]
                number = str(strng[:char])[::-1] if strng[:char] != '' else '0'
                znumber = str(int(number)+1).zfill(len(number))
                return word+znumber
    else:
        return "1"


print(increment_string('foobar100'))
increment_string('foobar')
increment_string('foobar0100')
print(increment_string(''))