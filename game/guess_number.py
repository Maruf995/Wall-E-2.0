import random
number = random.randint(0,11)

while True:
    human = int(input("Выбери: "))

    if number == human:
        print("Ты угадал!")
        break 
    else:
        print("Нет")