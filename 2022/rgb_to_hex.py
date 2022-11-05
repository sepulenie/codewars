def hexing(int):
    hexint = str((hex(int))[2:]).upper()
    return "0"+hexint if len(hexint) == 1 and int >= 0 else "00" if int < 0 else "FF" if int > 255 else hexint

def rgb(r, g, b):
    return hexing(r)+hexing(g)+hexing(b)

print(rgb(11,12,13))
