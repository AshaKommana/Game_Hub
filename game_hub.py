import random
import math

# ================================
# HANGMAN
# ================================
easy_words = ["apple", "ball", "cat", "dog", "fish", "milk", "tree", "book", "pen", "star"]
medium_words = ["guitar", "python", "planet", "camera", "rocket", "school", "friend", "jungle", "winter", "summer"]
hard_words = [
    "abruptly", "blizzard", "crypt", "daiquiri", "embezzle", "flapjack", "galvanize", "haiku", 
    "mnemonic", "nightclub", "pneumonia", "quorum", "rhythm", "sphinx", "triphthong", "wristwatch", "xylophone", "zephyr"
]

def choose_word(level):
    if level == "easy":
        return random.choice(easy_words)
    elif level == "medium":
        return random.choice(medium_words)
    else:
        return random.choice(hard_words)

def display_word(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def draw_hangman(attempts):
    stages = [
        "--------\n|      |\n|      O\n|     /|\\\n|     / \\\n|",
        "--------\n|      |\n|      O\n|     /|\\\n|     /",
        "--------\n|      |\n|      O\n|     /|\\",
        "--------\n|      |\n|      O\n|     /|",
        "--------\n|      |\n|      O\n|      |",
        "--------\n|      |\n|      O",
        "--------\n|      |"
    ]
    return stages[6 - attempts]

def hangman():
    print("\n🎮 Welcome to Hangman!")
    level = input("Choose difficulty (easy/medium/hard): ").lower()
    chosen_word = choose_word(level)
    guessed_letters = []
    attempts = 6

    while True:
        print(draw_hangman(attempts))
        print("Word:", display_word(chosen_word, guessed_letters))
        print("Attempts left:", attempts)

        if display_word(chosen_word, guessed_letters) == chosen_word:
            print("🎉 You guessed the word:", chosen_word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("⚠️ Already guessed.")
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            attempts -= 1
            print("❌ Wrong guess.")

            if attempts == 0:
                print("💀 Out of attempts. The word was:", chosen_word)
                break


# ================================
# MATH QUIZ
# ================================
def math_quiz():
    print("\n🧮 Welcome to Math Quiz!")
    score = 0
    operations = ["+", "-", "*", "/", "%", "**", "sqrt"]

    for _ in range(5):
        op = random.choice(operations)

        if op == "sqrt":
            a = random.randint(1, 100)
            print(f"√{a} = ? (Round to 2 decimals)")
            correct = round(math.sqrt(a), 2)
        else:
            a, b = random.randint(1, 20), random.randint(1, 20)
            question = f"{a} {op} {b}"
            correct = round(eval(question), 2)
            print(f"{question} = ? (Round to 2 decimals if needed)")

        try:
            ans = float(input("Your answer: "))
            if abs(ans - correct) < 0.01:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong. Correct: {correct}")
        except:
            print("⚠️ Invalid input.")

    print(f"Final Score: {score}/5")


# ================================
# TIC TAC TOE
# ================================
def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print()

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row): return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2-i] == player for i in range(3)): return True
    return False

def tic_tac_toe():
    print("\n⭕❌ Welcome to Tic Tac Toe!")
    mode = input("Play vs (1) Player or (2) Computer? ")
    board = [[" "]*3 for _ in range(3)]
    current = "X"

    for _ in range(9):
        print_board(board)

        if mode == "2" and current == "O":
            # simple AI: choose winning move, else random
            move = None
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        if check_winner(board, "O"):
                            move = (i, j)
                        board[i][j] = " "
            if not move:
                empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
                move = random.choice(empty)
            i, j = move
            print("🤖 Computer chooses:", i+1, j+1)
        else:
            try:
                i, j = map(int, input(f"Player {current}, enter row and col (1-3): ").split())
                i, j = i-1, j-1
                if board[i][j] != " ":
                    print("⚠️ Spot taken, try again.")
                    continue
            except:
                print("⚠️ Invalid input.")
                continue

        board[i][j] = current
        if check_winner(board, current):
            print_board(board)
            print(f"🎉 Player {current} wins!")
            return
        current = "O" if current == "X" else "X"

    print_board(board)
    print("🤝 It's a draw!")


# ================================
# GUESS THE NUMBER
# ================================
def guess_number():
    print("\n🔢 Welcome to Guess the Number!")
    level = input("Choose difficulty (easy/medium/hard): ").lower()
    if level == "easy":
        number = random.randint(1, 20)
        tries = 6
    elif level == "medium":
        number = random.randint(1, 50)
        tries = 8
    else:
        number = random.randint(1, 100)
        tries = 10

    while tries > 0:
        try:
            guess = int(input(f"Enter your guess (Attempts left {tries}): "))
            if guess == number:
                print("🎉 Correct! You guessed the number.")
                return
            elif guess < number:
                print("⬆️ Too low!")
            else:
                print("⬇️ Too high!")
            tries -= 1
        except:
            print("⚠️ Invalid input.")

    print(f"💀 Out of attempts! The number was {number}.")


# ================================
# MAIN HUB
# ================================
def game_hub():
    while True:
        print("\n🎮 Mini Game Hub")
        print("1. Hangman")
        print("2. Math Quiz")
        print("3. Tic Tac Toe")
        print("4. Guess the Number")
        print("5. Exit")

        choice = input("Choose a game: ")

        if choice == "1":
            hangman()
        elif choice == "2":
            math_quiz()
        elif choice == "3":
            tic_tac_toe()
        elif choice == "4":
            guess_number()
        elif choice == "5":
            print("👋 Thanks for playing!")
            break
        else:
            print("⚠️ Invalid choice.")

# Run hub
if __name__ == "__main__":
    game_hub()
