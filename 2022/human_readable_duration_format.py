def format_duration(input_seconds):
    def stringofication(input):
        value, name = str(input[0]), input[1]
        if value != '0':
            string = value+' '+name+'s' if value[-1] in ['0', '2', '3', '4', '5', '6', '7', '8', '9'] or (len(value) > 1 and value[-2] == '1') else value+' '+name
            return string
    seconds = input_seconds
    year = [(seconds//31536000), 'year']
    day = [((seconds - (31536000*year[0]))//86400), 'day']
    hour = [(seconds - (31536000*year[0]) - (86400*day[0]))//3600, 'hour']
    minute = [(seconds - (31536000*year[0]) - (86400*day[0]) - (3600*hour[0]))//60, 'minute']
    second = [(seconds - (31536000*year[0]) - (86400*day[0]) - (3600*hour[0]) - (60*minute[0])), 'second']
    return list(map(stringofication, filter(lambda n: n[0] != 0, [year, day, hour, minute, second])))

print(format_duration(50004545450))