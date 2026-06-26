import random

def play_hangman():

    words = ["python", "computer", "programming", "developer", "keyboard"]

    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6

    print("\n🎮 Welcome to Hangman Game!")
    print("Guess the word one letter at a time.")
    print(f"You have {max_attempts} wrong attempts.\n")

    while wrong_guesses < max_attempts:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed letters:", guessed_letters)
        print("Remaining attempts:", max_attempts - wrong_guesses)

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You won!")
            print("The word was:", word)
            break

    else:
        print("\n😢 Game Over!")
        print("The word was:", word)


while True:
    play_hangman()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for playing! 👋")
        break