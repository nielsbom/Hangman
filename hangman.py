# Hangman
# Guess letters, then guess the word.
# http://en.wikipedia.org/wiki/Hangman_(game)

# standard library
import sys, os, random

# custom modules
import graphics

# clears the screen
def clear():
    os.system("clear")


# get a random word
def getRandomWord(source, wordLength=5):
    while True:
        word = random.choice(words).strip()
        if len(word) == wordLength:
            return word


def victory():
    print "Congratulations, you guessed the word correctly!"


def areAllLettersGuessed(word, guessedLetters):
    # remove duplicates from word
    wordNoDuplicates = list(set(word))

    correctLetters = [letter for letter in guessedLetters if letter in word]

    if len(correctLetters) == len(wordNoDuplicates):
        return True
    else:
        return False


# load the words in the dictionary
file = open("dutch.txt", "r+")  # open for reading and writing
words = file.readlines()

# introduction
clear()
print """Welcome to Hangman

The goal of this game is to find out which word I'm thinking of.
You can guess for a letter or a complete word. You can guess wrong 6
times, the 7th wrong guess will be your last mistake.
"""

gamePlayed = False
while True:
    # start a new game?
    if not gamePlayed:
        newGameQuestion = "Are you ready to start?"
    else:
        newGameQuestion = "Do you want to play another game?"
    input = raw_input(newGameQuestion + " (y/n) \n")

    if input == "n":
        clear()
        break
    elif input != "y":
        clear()
        print "Please press either a 'y' or an 'n'"
        continue

    # how long should the word be?
    wordLength = int(raw_input("How many letters do you want to guess for?"))

    # start the game
    word = getRandomWord(words, wordLength)
    guessedLetters = []  # all the letters that were guessed
    mistakes = 0

    while mistakes < 8:
        clear()
        if guessedLetters:
            print "Guessed letters: ",
            for letter in guessedLetters:
                print letter + " ",

        print graphics.hangmanSteps[mistakes] + "\n\n"

        if mistakes < 7:
            print "Guess this word: ",

            for letter in word:
                if letter in guessedLetters:
                    print letter,
                else:
                    print "_",

            print ("\n")
            print "You have " + str(7 - mistakes) + " guesses left"

            guess = raw_input("Guess a letter or the complete word: ")

            # guess a letter
            if len(guess) == 1:
                if guess not in guessedLetters:
                    guessedLetters.append(guess)
                    if guess not in word:
                        mistakes += 1
                    else:
                        # if all letters are guessed, player wins
                        if areAllLettersGuessed(word, guessedLetters):
                            victory()
                            break

                else:
                    raw_input(
                        "You already guessed that letter, press Enter to guess another one"
                    )
                    continue

            # guesses for the whole word
            else:
                if len(guess) != len(word):
                    pass
                if len(guess) == len(word):
                    mistakes += 1
                    if guess == word:
                        victory()
                        break

        else:
            print "Game over, too bad\n"
            print 'The correct word was "' + word + '"\n\n'
            break
    gamePlayed = True

if gamePlayed:
    print "Thanks for playing Hangman!\n\n"

print "This game was made by Niels Bom 2011-09-20"
