import math
import random

# Описание правил игры
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def generate_round_data():
    n = random.randint(1, 100)
    question = str(n)

    # Определяем правильный ответ
    correct_answer = "yes" if is_prime(n) else "no"

    return question, correct_answer