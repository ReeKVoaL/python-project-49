from brain_games.engine import run_game
from brain_games.games.progression import RULES, generate_round_data


def main():
    run_game(RULES, generate_round_data)


if __name__ == "__main__":
    main()