def format_duration(input_seconds):
    if input_seconds == 0: return 'now'
    def stringofication(input):
        value, name = input[0], input[1]
        if value != '0':
            string = str(value)+' '+name+'s' if value > 1 else str(value)+' '+name
            return string
    seconds = input_seconds
    year = [(seconds//31536000), 'year']
    day = [((seconds - (31536000*year[0]))//86400), 'day']
    hour = [(seconds - (31536000*year[0]) - (86400*day[0]))//3600, 'hour']
    minute = [(seconds - (31536000*year[0]) - (86400*day[0]) - (3600*hour[0]))//60, 'minute']
    second = [(seconds - (31536000*year[0]) - (86400*day[0]) - (3600*hour[0]) - (60*minute[0])), 'second']
    numlist = list(map(stringofication, filter(lambda n: n[0] != 0, [year, day, hour, minute, second])))
    fstring = ''
    for n in range(0, len(numlist)):
        if n < len(numlist)-2:
            fstring = fstring+(str(numlist[n])+', ')
        elif n == len(numlist)-2:
            fstring = fstring+(str(numlist[n])+' and ')
            break
    fstring = fstring+(str(numlist[len(numlist)-1]))
    return fstring
print(format_duration(23453464745747456456))