import random


number = random.randint(0,10)

while True:
    answer = input("Введите число:")
    if not answer or answer == "exit":
        break
    if not answer.isdigit():
        print("Введите правильное число!")
        continue
    user_answer = int(answer)

    if user_answer > number:
        print("Загаданное число меньше")
    elif user_answer < number:
        print("Загаданное число больше")
    else:
        while True:
            rpt = input("Вы угадали! начать еще раз? д/н")
            if not rpt:
                continue
            elif rpt == "д" or rpt == "да":
                number = random.randint(0, 10)
                break
            elif rpt =="н" or rpt == "нет":
                break
        break