from game import DIFFICULTIES, Minesweeper

if __name__ == "__main__":
    choices = {"1": "easy", "2": "medium", "3": "hard"}
    print("Select difficulty:")
    for number, difficulty in choices.items():
        rows, cols, mines = DIFFICULTIES[difficulty]
        print(f"{number}. {difficulty.title()} ({rows}x{cols}, {mines} mines)")

    while True:
        choice = input("Difficulty [1-3]: ").strip()
        if choice in choices:
            break
        print("Please choose 1, 2, or 3.")

    Minesweeper(choices[choice]).run()
