def scream():
    print("я хуй бля")

def dosomethingbefore(func):
    print("Я делаю что-то еще, перед тем как вызвать функцию которую ты мне передал")
    print(func())


dosomethingbefore(scream)