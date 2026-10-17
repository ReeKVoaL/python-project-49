import prompt


def run_game(game_description, generate_round_data):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_description)

    # Константа количества раундов, единая для всех игр
    correct_answers_count = 0
    required_wins = 3

    while correct_answers_count < required_wins:

        # Получаем данные для текущего раунда из модуля игры
        question, correct_answer = generate_round_data()
        # Показываем выражение пользователю
        print(f"Question: {question}")

        # Получаем ответ пользователя
        user_answer = prompt.string("Your answer: ").strip()

        # Проверяем ответ
        match user_answer:
            case _ if user_answer == str(correct_answer):
                print("Correct!")
                correct_answers_count += 1
            case _:
                # Вывод в случае неверного ответа и завершение игры
                print(
                    f"'{user_answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_answer}'."
                    )
                print(f"Let's try again, {name}!")
                return  # Выход из функции (завершение игры)

    # Если цикл завершился и игрок не ошибся — он победил
    print(f"Congratulations, {name}!")