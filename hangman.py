# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    correct_guesses = 0
    for char in secretWord:
        if char not in lettersGuessed:
            return False
        else:    
            correct_guesses += 1
    if correct_guesses == len(secretWord):
        return True    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess_status = ""
    for char in secretWord:
        if char in lettersGuessed:
            guess_status += char + " "
        else:
            guess_status += " _ "
    return guess_status    




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    available_letters = list(string.ascii_lowercase)
    for c in lettersGuessed:
        if c in available_letters:
            available_letters.remove(c)
        else:
            continue
    return "".join(available_letters)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    number_of_guesses = 8
    available_letters = list(string.ascii_lowercase)
    guessedsofar = ""
    lettersGuessed = ""
    

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    
    while number_of_guesses > 0:
        print("-------------")
        print("You have", number_of_guesses, "guesses left.")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        userGuessed = input("Please guess a letter: ")
        lettersGuessed += userGuessed

        if userGuessed in guessedsofar:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        
        elif userGuessed in secretWord:
            print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print("-------------")
                print("Congratulations, you won!")
                break
                           
        elif userGuessed not in secretWord:
            number_of_guesses -= 1
            getAvailableLetters(lettersGuessed)
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
            if number_of_guesses == 0:
                print("-------------")
                print("Sorry, you ran out of guesses, The word was", secretWord, ".")
                break
        guessedsofar += userGuessed

hangman("zzzzzz")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)
