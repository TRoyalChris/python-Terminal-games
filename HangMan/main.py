import random
import asciiArt
import words


wordThisRound = random.choice(words.wordsInList)
placeHolder = ""
lives = 0

for letter in wordThisRound:
    placeHolder += "_"

print(wordThisRound)
print(placeHolder)

wordComplete = False
letters = []
print("Welcome to Hangman, good luck...")
while not wordComplete and lives < 6:
    print(f"*********** {lives}/ 6 Lives wasted ***********")
    guessed_word = input("Choose a letter: ").lower()
    if guessed_word  in letters:
        print(f"The Letter {guessed_word} was already guessed")
        continue
    letters.append(guessed_word)
    display = ""
    if guessed_word not in wordThisRound:
        lives += 1
        print(f"The Letter {guessed_word} was not in the word")

    for letter in wordThisRound:
        if letter in letters:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        wordComplete = True
        print("You Win!")


    print(display)
    print(asciiArt.hangman_stages[lives])
if lives == 6:
    wordComplete = True
    print("Game Over")
