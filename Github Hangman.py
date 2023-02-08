import random

def display_word(word, letters_guessed):
    display = ""
    for letter in word:
        if letter in letters_guessed:
            display += letter
        else:
            display += "-"
    return display

def hangman(word):
    letters_guessed = []
    strikes = 0
    display = display_word(word, letters_guessed)
    print("Welcome to Hangman!\n")
    print("Type 'quit' at any time to end the game.\n")
    print("The word is: " + display + "\n")
    while strikes < 5 and "-" in display:
        letter = input("Guess a letter or the word: ").upper()
        if letter.upper() == "QUIT":
            print("You quit the game.\n")
            return None
        if letter == word:
            print("You won!\n")
            return None
        if letter in word and letter not in letters_guessed:
            letters_guessed.append(letter)
            display = display_word(word, letters_guessed)
            print("\n" + display + "\n")
        elif letter in letters_guessed:
            print("You already guessed that letter. Try again.\n")
        else:
            strikes += 1
            print("Incorrect. You have " + str(5 - strikes) + " strikes left.\n")
    if strikes == 5:
        print("You lost.\n")
    else:
        print("You won!\n")

words = ["DRAGON", "KNIGHT", "PRINCESS", "WIZARD", "CASTLE"]
while True:
    word = random.choice(words).upper()
    result = hangman(word)
    if result == None:
        break
