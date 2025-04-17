import random

rps_words = ['Камень', 'Ножницы', 'Бумага'\
             'камень', 'ножницы', 'бумага']

while True:
    rps_choice = random.choice(rps_words)  # Выбираем один элемент, а не список
    human = input("Выбери: ")

    if human not in rps_words:
        print("Неправильный ввод!")

    if (rps_choice == "Камень" and human == "Ножницы") or \
       (rps_choice == "Ножницы" and human == "Бумага") or \
       (rps_choice == "Бумага" and human == "Камень"):
        print(f"Ты проиграл! Я выбрал {rps_choice}")
    elif rps_choice == human:
        print(f"Ничья! Я выбрал {rps_choice}")
    else:
        print(f"Ты выиграл! Я выбрал {rps_choice}")
