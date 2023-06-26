import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
display = []
guesses = []

print(logo)

chosen_word = random.choice(word_list)

for _ in chosen_word:
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(f"You already guessed {guess.upper()}.")
    else:
        if guess in chosen_word:
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            guesses.append(guess)
            print(display)
        else:
            lives -= 1
            guesses.append(guess)
            print(stages[lives])
            print(display)
            print(f"{guess.upper()} is not in the word.")

    if lives == 0:
        end_of_game = True
        print(f"You lose! The word was '{chosen_word}'.")
    if "_" not in display:
        end_of_game = True
        print("You win!")
