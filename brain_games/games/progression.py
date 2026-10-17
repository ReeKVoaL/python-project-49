import random

# Описание правил игры
RULES = "What number is missing in the progression?"


def generate_round_data():
    start = random.randint(1, 50)  # Начальное число прогрессии
    step = random.randint(1, 10)  # Шаг прогрессии
    length = 10  #Длина прогрессии

    # Создаем список чисел арифметической прогрессии
    progression = [str(start + i * step) for i in range(length)]

    # Выбираем случайный индекс элемента, который нужно спрятать
    hidden_index = random.randrange(length)

    # Сохраняем правильный ответ перед тем, как спрятать элемент
    correct_answer = progression[hidden_index]

    # Заменяем выбранный элемент на две точки
    progression[hidden_index] = ".."

    # Формируем строку вопроса, объединяя элементы через пробел
    question = " ".join(progression)

    return question, correct_answer