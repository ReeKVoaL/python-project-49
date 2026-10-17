import math
import random

# Описание правил игры
RULES = 'Find the greatest common divisor of given numbers.'


def generate_round_data():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"

    correct_answer = math.gcd(num1, num2)

    return question, correct_answer  # Выход из функции (завершение игры)