def sum_strings(x, y):
    dick = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
    xrev, yrev = x[::-1], y[::-1]
    longest = max([xrev,yrev], key=len)
    answer = ''
    
    def summa(i):




    for i in range (0, len(longest)):
        res = dick[x[i]]+dick[y[i]]
        if res < 10:
            answer.join(str(res))
        else:
            answer.join(str(res))
        print(res)






sum_strings("1","1")
sum_strings("13","13")
#sum_strings("123","99")
#sum_strings("412","77")
