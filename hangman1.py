# 1. what's your name
# 2. randomise a word
# 3. draw a board
# 4. take an input from the user
# 5. check if the letter exists in the word
# 6. display the result
# 7. save the result

import random
from random_word import RandomWords

r = RandomWords()

# ask user for their name
username = input("What is your name: ")

while True:
    # the player can choose the difficulty level which the length of the word and the number of lives is going to
    # based on
    print("Which difficulty level would you like? easy/medium/hard")

    while True:
        difficulty = input("Enter e, m or h: ")
        letter_count = []

        if difficulty == "e":
            lives = 9
            letter_count = [1, 7]
        elif difficulty == "m":
            lives = 6
            letter_count = [7, 11]
        elif difficulty == "h":
            lives = 3
            letter_count = [11, 40]
        else:
            print("That is not a correct answer.")
            continue

        break

    # choose a word from the list
    while True:
        word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective",
                                 minCorpusCount=1000, minDictionaryCount=20, minLength=letter_count[0],
                                 maxLength=letter_count[1])
        # noticed that the get_random_word() returns None from time to time
        if word is None:
            continue
        else:
            break

    # number of letters guessed correctly by the player
    correct_guesses = 0

    # create a board
    board = []
    for i in range(len(word)):
        board += "_"

    # set a list with messages that are going to be displayed when the player succeeds
    success_message = [
        "Good job!",
        "Nice one!",
        "Right there!",
        "Sexy brain ;)"
    ]
    missed_message = [
        "Not this time. ",
        "Try again. ",
        "Almost. "
    ]
    win_message = [
        "Amazing, you won" + username + "! ",
        "Great job " + username + "! ",
        "You beat me " + username + ". ",
    ]
    loose_message = [
        "You lost your lives :( ",
        "You did not win this time " + username + ". ",
        "You got hanged " + username + ". "
    ]

    # greeting
    print("Hi " + username + "!")
    print("We are going to play a game called hangman. The word has " + str(len(word)) + " letters and you have " + str(lives) + " lives.")

    while lives > 0 and not(correct_guesses == len(word)):
        # board
        print(''.join(board))

        # take an input from the user
        print("Enter # to attempt guessing the whole word.")
        user_letter = input("Write a letter: ")

        # lower-case it just in case ;)
        user_letter = user_letter.lower()

        # check if the letter is in the word
        if user_letter in word:
            # go through all letters in the word to find where it is
            for letter_index in range(len(word)):
                # if you find a match then increase the correct guesses count and add the letter to the board
                if user_letter == word[letter_index]:
                    correct_guesses += 1
                    board[letter_index] = word[letter_index]
            if not correct_guesses == len(word):
                print(random.choice(success_message))
        elif user_letter == "#":
            # let the user guess the whole word if he enters #
            word_guess = input("Enter the word: ")
            if word_guess == word:
                # set the number of correct guesses to max when the player guessed the word
                correct_guesses = len(word)
            else:
                lives -= 1
                if not lives == 0:
                    print(random.choice(missed_message) + "You have " + str(lives) + " lives left.")
        else:
            # if the letter doesn't appear to be in the word, subtract live from the lives count
            lives -= 1
            if not lives == 0:
                print(random.choice(missed_message) + "You have " + str(lives) + " lives left.")

    # display the win/lose message to the player
    if lives == 0:
        print("The word was '" + word + "'.")
        print(random.choice(loose_message) + "Would you like to try again? Y/N")
    else:
        print(random.choice(win_message) + "Would you like to try again? Y/N")

    if input() == "Y":
        continue
    else:
        break

