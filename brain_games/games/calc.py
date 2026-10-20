import random

# Описание правил игры
RULES = "What is the result of the expression?"


def generate_round_data():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    # Список доступных математических операций
    operators = ["+", "-", "*"]
    operator = random.choice(operators)

    # Вычисляем правильный ответ в зависимости от операции
    match operator:
        case "+":
            correct_answer = num1 + num2
        case "-":
            correct_answer = num1 - num2
        case "*":
            correct_answer = num1 * num2

        # Показываем выражение пользователю
    question = f"{num1} {operator} {num2}"

    return question, correct_answer