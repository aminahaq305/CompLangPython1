# Amina Haq | Project 6 | Playing around with Python

# import random module used later to generate random word
import random


# generates hash with list of words with lengths as keys from wordlist file
# accepts a word and the wordlist hash
def splitlist(word, wordlist):
    # if the wordlist hash contains a list of the length of the word
    # then append the word to that list, else create new list and append
    if len(word) not in wordlist:
        wordlist[len(word)] = [word]
    elif len(word) in wordlist:
        wordlist[len(word)] += [word]


wordlist = {}  # hash to hold all words with lengths as keys
wordLength = 0  # length of word to be guessed
guesses = int(10)  # maximum number of guesses
gameOver = False  # checks whether word has been guessed
wordsGuessed = []  # list to hold words or letters that have been guessed

# open the wordlist.txt file but if not found throw exception and exit gracefully
try:
    words = open('wordlist.txt', 'r')
except FileNotFoundError:
    print("Oops: wordlist file was not found!")
# if file found, commence game play
else:
    # this for loop takes every word in the wordlist file
    # and adds it to the hash using the function 'splitlist' defined earlier
    for line in words:
        for word in line.split():
            splitlist(word, wordlist)
    max_key = max(wordlist, key=wordlist.get)  # holds the length of the largest word in the wordlist file
    print('Welcome to Hangman!')  # Welcome to user
    while wordLength < 2 or max_key < wordLength:
        # repeat this block of code while length is incorrect
        try:
            # prompt user for word length
            wordLength = int(input('What length word would you like me to choose? ==> '))
            if wordLength < 2 or max_key < wordLength:
                # output error, if word length is incorrect
                # iterate through while loop
                print('Invalid length, please enter a value greater than 2 and less than ' + str(max_key) + '\n')
        except ValueError:
            # if word length is not an integer, output error
            # and iterate through the while loop
            print('Incorrect input. Please try again! \n')
            pass
    # once valid length is entered, generate a random word of that length
    # using the random.choice function
    blank = random.choice(wordlist[wordLength])
    # create a string of asterisks of the length entered
    toGuess = '*' * wordLength
    # repeat this block of code, while word has not been guessed
    # and player is not out of guesses
    while guesses > 0 and gameOver is False:
        print('\nWord: ' + toGuess)  # print the string of asterisks
        if guesses == 1:  # if it is the last guess, remind the user
            print('This is your last guess!')
        else:
            # output number of guesses remaining
            print('You have ' + str(guesses - 1) + ' guesses remaining.')
        # accept a word or letter
        wordGuessed = input('Type a letter or a word guess: ')
        # if the word has already been guessed, remind the user
        if wordGuessed in wordsGuessed:
            print('You have already guessed ' + wordGuessed + '!')
        else:
            # add the word or letter guessed to a list to keep track
            wordsGuessed += wordGuessed
            # execute this block of code if a letter is guessed
            if len(wordGuessed) == 1:
                # if the letter is in the word to be guessed
                if wordGuessed in blank:
                    # output the number of occurrences of that letter
                    if blank.count(wordGuessed) == 1:
                        print('There is ' + str(blank.count(wordGuessed)) + ' ' + wordGuessed + '!')
                    else:
                        print('There are ' + str(blank.count(wordGuessed)) + ' ' + wordGuessed + 's!')
                    # update the asterisk string to contain the letter guessed
                    # wherever that letter is in the word
                    for i, letter in enumerate(blank):
                        if wordGuessed == letter:
                            temp = list(toGuess)
                            temp[i] = wordGuessed
                            toGuess = "".join(temp)
                # otherwise, if the letter is not in the word, output message
                else:
                    print('Sorry, there are no ' + wordGuessed + 's.')
            # if a whole word is guessed
            else:
                # if the word guessed is correct, gameOver is true
                if wordGuessed == blank:
                    gameOver = True
                # if the word guessed is incorrect, output message
                else:
                    print('Sorry, the word is not ' + wordGuessed)
            # decrement number of guesses
            guesses -= 1
            # if there are no blanks left in the string to be guessed
            # gameOver is true
            if '*' not in toGuess:
                gameOver = True
    # if the user was able to guess the word within the guesses, output Congratulatory message
    if gameOver is True:
        print('\nCongratulations, you guessed it!\nGame over.')
    # if the user was unable to guess the word within the guesses, output "you lost" message
    else:
        print('\nYou are out of guesses, you lost!\nGame over.')
