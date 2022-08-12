from dataclasses import replace
import random
from os import system, name
from time import sleep

def clear():
    _=system('clear')

random.seed(a=None, version=2)


hangmanStages = [
    
    '''            |=======|
            |       |      
                    | 
                    |
                    |
              ______|______
    ''',
        '''            |=======|
            |       |      
            O       | 
                    |
                    |
              ______|______
    ''',
        '''            |=======|
            |       |      
            O       | 
            |       |
                    |
              ______|______
    ''',
        '''            |=======|
            |       |      
            O       | 
           -|       |
                    |
              ______|______
    ''',
        '''            |=======|
            |       |      
            O       | 
           -|-      |
                    |
              ______|______
    ''',
        '''            |=======|
            |       |      
            O       | 
           -|-      |
            /       |
              ______|______
    ''',
        '''            |=======|       
            |       |       
            O       |       
           -|-      |       
            /\      |       
              ______|______ 
    ''',
    ''' 
      ___       ___           ___           ___           ___     
     /\__\     /\  \         /\  \         /\  \         /\  \    
    /:/  /    /::\  \       /::\  \       /::\  \       /::\  \   
            |=======|          /:/  /    /:/\:\  \     /:/\ \  \     /:/\:\  \     /:/\:\  \  
            |       |         /:/  /    /:/  \:\  \   _\:\~\ \  \   /::\~\:\  \   /::\~\:\  \ 
            O       |        /:/__/    /:/__/ \:\__\ /\ \:\ \ \__\ /:/\:\ \:\__\ /:/\:\ \:\__\ 
           -|-      |        \:\  \    \:\  \ /:/  / \:\ \:\ \/__/ \:\~\:\ \/__/ \/_|::\/:/  /
            /\      |         \:\  \    \:\  /:/  /   \:\ \:\__\    \:\ \:\__\      |:|::/  / 
              ______|______    \:\  \    \:\/:/  /     \:\/:/  /     \:\ \/__/      |:|\/__/  
                                \:\__\    \::/  /       \::/  /       \:\__\        |:|  |    
                                 \/__/     \/__/         \/__/         \/__/         \|__|    ''',
        '''      ___                       ___           ___           ___           ___     
     /__/\        ___          /__/\         /__/\         /  /\         /  /\    
    _\_ \:\      /  /\         \  \:\        \  \:\       /  /:/_       /  /::\   
   /__/\ \:\    /  /:/          \  \:\        \  \:\     /  /:/ /\     /  /:/\:\  
  _\_ \:\ \:\  /__/::\      _____\__\:\   _____\__\:\   /  /:/ /:/_   /  /:/~/:/  
 /__/\ \:\ \:\ \__\/\:\__  /__/::::::::\ /__/::::::::\ /__/:/ /:/ /\ /__/:/ /:/___
 \  \:\ \:\/:/    \  \:\/\ \  \:\~~\~~\/ \  \:\~~\~~\/ \  \:\/:/ /:/ \  \:\/:::::/
  \  \:\ \::/      \__\::/  \  \:\  ~~~   \  \:\  ~~~   \  \::/ /:/   \  \::/~~~~ 
   \  \:\/:/       /__/:/    \  \:\        \  \:\        \  \:\/:/     \  \:\     
    \  \::/        \__\/      \  \:\        \  \:\        \  \::/       \  \:\    
     \__\/                     \__\/         \__\/         \__\/         \__\/    ''',
        '''      ___           ___           ___           ___           ___     
     /  /\         /  /\         /  /\         /  /\         /  /\    
    /  /:/_       /  /::\       /  /::\       /  /::\       /  /::\   
   /  /:/ /\     /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\  
  /  /:/ /:/_   /  /:/~/:/    /  /:/~/:/    /  /:/  \:\   /  /:/~/:/  
 /__/:/ /:/ /\ /__/:/ /:/___ /__/:/ /:/___ /__/:/ \__\:\ /__/:/ /:/___
 \  \:\/:/ /:/ \  \:\/:::::/ \  \:\/:::::/ \  \:\ /  /:/ \  \:\/:::::/
  \  \::/ /:/   \  \::/~~~~   \  \::/~~~~   \  \:\  /:/   \  \::/~~~~ 
   \  \:\/:/     \  \:\        \  \:\        \  \:\/:/     \  \:\     
    \  \::/       \  \:\        \  \:\        \  \::/       \  \:\    
     \__\/         \__\/         \__\/         \__\/         \__\/    ''',
        '''      ___           ___           ___           ___           ___           ___           ___     
     /__/\         /  /\         /__/\         /  /\         /__/\         /  /\         /__/\    
     \  \:\       /  /::\        \  \:\       /  /:/_       |  |::\       /  /::\        \  \:\   
      \__\:\     /  /:/\:\        \  \:\     /  /:/ /\      |  |:|:\     /  /:/\:\        \  \:\  
  ___ /  /::\   /  /:/~/::\   _____\__\:\   /  /:/_/::\   __|__|:|\:\   /  /:/~/::\   _____\__\:\ 
 /__/\  /:/\:\ /__/:/ /:/\:\ /__/::::::::\ /__/:/__\/\:\ /__/::::| \:\ /__/:/ /:/\:\ /__/::::::::\
 \  \:\/:/__\/ \  \:\/:/__\/ \  \:\~~\~~\/ \  \:\ /~~/:/ \  \:\~~\__\/ \  \:\/:/__\/ \  \:\~~\~~\/
  \  \::/       \  \::/       \  \:\  ~~~   \  \:\  /:/   \  \:\        \  \::/       \  \:\  ~~~ 
   \  \:\        \  \:\        \  \:\        \  \:\/:/     \  \:\        \  \:\        \  \:\     
    \  \:\        \  \:\        \  \:\        \  \::/       \  \:\        \  \:\        \  \:\    
     \__\/         \__\/         \__\/         \__\/         \__\/         \__\/         \__\/    '''
]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra kush ayush rupesh jaivish shivom adi heeya deeya mahitha rhea prachi vrunda krishna'.split()

#selects word write for hangman
def getWord(wordList):
    worldSelect = random.randint(0,len(wordList))
    return wordList[worldSelect]

def printDisplay(wrongGuesses, guesses):
    print(hangmanStages[wrongGuesses])
    print()
    print("Guessed Letters: ", end='')
    for guess in guesses:
        print(guess, " ", end='')
    printCurrGuess(currGuess)
    
def guessLetter(word, wrongGuesses, currGuess):
    guess = input("Guess a Letter: ")
    if guess in guesses:
        repeatGuess()
    else:
        guesses.append(guess)
        if guess in word:
            i = 0
            for l in word:
               if guess == l:
                  currGuess = setCurrGuess(currGuess, i, guess)
               i+=1
        else:
            print("WRONG!!!!")
            wrongGuesses+=1
    return(currGuess, wrongGuesses)
    
def setCurrGuess(currGuess, place, guess):
    currGuess=currGuess.replace(" ", "")
    currGuessList = list(currGuess)
    currGuessList[place] = guess
    currGuess = " ".join(currGuessList)
    return currGuess

def printCurrGuess(currGuess):
    print()
    print()
    print(currGuess)
    print()
    print()
    
def guessWord(word):
    return

def winnnerSc(gameWords):
    print(hangmanStages[8])
    print()
    print("WINNER WINNER CHICKEN DINNER!")
    print("YOU GUESSED THE WORD ", gameWords, " CORRECTLY!")

def loserSc():
    print(hangmanStages[7])
    print()
    print("THE WORD WAS " + gameWord + "!")

def displayLetters():
    return

def repeatGuess():
    print("YOU CANNOT GUESS A LETTER TWICE")

play = True

while play:
    
    guesses = []
    
    gameWord = getWord(words)
    print(gameWord)
    wrongGuesses = 0
    
    currGuess = ""
    for letter in gameWord:
        currGuess = currGuess + '_ '
    
    while wrongGuesses < 6:
        print()
        printDisplay(wrongGuesses, guesses)
        currGuessTest = currGuess.replace(" ","")
        if currGuessTest==gameWord:
            winnnerSc(gameWord)
            break
        else:
            pass
        retTup = guessLetter(gameWord, wrongGuesses, currGuess)
        currGuess = retTup[0]
        wrongGuesses = retTup[1]
        sleep(1)
        clear()
        
    if wrongGuesses == 6:
        loserSc(gameWord)
        
    #if guess wrong letter throw wrong screen, right screen

        
    
    print()
    print()
    ans = input("Enter 'yes' to play again, leave blank to quit:    ")
    if ans == "yes":
        wrongGuesses=0
    else:
        play = False


