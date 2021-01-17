import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed a letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"\nYOU LOSE!\nThe word: {chosen_word}\n")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")

    print(hangman_art.stages[lives])
