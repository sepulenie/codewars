def sqrt_approximation(number):
    k = 1
    l = number
    for i in range(1, number):
        l = l - k
        if l-k > 1:
            k += 2
        else:
            if l != 0:
                print(number, " - ", [i, i+1])
                return [i, i+1]
            else:
                print(number, " - ", i)
                return i


for i in range (1, 900):
    sqrt_approximation(i)