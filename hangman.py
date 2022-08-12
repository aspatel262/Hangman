from dataclasses import replace
from operator import truediv
import random
from os import system, name
from time import sleep
from turtle import title

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
     \__\/         \__\/         \__\/         \__\/         \__\/         \__\/         \__\/    ''',
'''      ___           ___           ___           ___           ___           ___                 
     /  /\         /  /\         /  /\         /  /\         /  /\         /  /\          ___   
    /  /:/        /  /::\       /  /::\       /  /::\       /  /:/_       /  /:/         /  /\  
   /  /:/        /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/ /\     /  /:/         /  /:/  
  /  /:/  ___   /  /:/  \:\   /  /:/~/:/    /  /:/~/:/    /  /:/ /:/_   /  /:/  ___    /  /:/   
 /__/:/  /  /\ /__/:/ \__\:\ /__/:/ /:/___ /__/:/ /:/___ /__/:/ /:/ /\ /__/:/  /  /\  /  /::\   
 \  \:\ /  /:/ \  \:\ /  /:/ \  \:\/:::::/ \  \:\/:::::/ \  \:\/:/ /:/ \  \:\ /  /:/ /__/:/\:\  
  \  \:\  /:/   \  \:\  /:/   \  \::/~~~~   \  \::/~~~~   \  \::/ /:/   \  \:\  /:/  \__\/  \:\ 
   \  \:\/:/     \  \:\/:/     \  \:\        \  \:\        \  \:\/:/     \  \:\/:/        \  \:\ 
    \  \::/       \  \::/       \  \:\        \  \:\        \  \::/       \  \::/          \__\/
     \__\/         \__\/         \__\/         \__\/         \__\/         \__\/                ''',
'''      ___           ___           ___           ___           ___              
     /__/\         /  /\         /  /\         /__/\         /  /\             
    _\_ \:\       /  /::\       /  /::\        \  \:\       /  /:/_            
   /__/\ \:\     /  /:/\:\     /  /:/\:\        \  \:\     /  /:/ /\           
  _\_ \:\ \:\   /  /:/~/:/    /  /:/  \:\   _____\__\:\   /  /:/_/::\          
 /__/\ \:\ \:\ /__/:/ /:/___ /__/:/ \__\:\ /__/::::::::\ /__/:/__\/\:\         
 \  \:\ \:\/:/ \  \:\/:::::/ \  \:\ /  /:/ \  \:\~~\~~\/ \  \:\ /~~/:/         
  \  \:\ \::/   \  \::/~~~~   \  \:\  /:/   \  \:\  ~~~   \  \:\  /:/          
   \  \:\/:/     \  \:\        \  \:\/:/     \  \:\        \  \:\/:/           
    \  \::/       \  \:\        \  \::/       \  \:\        \  \::/            
     \__\/         \__\/         \__\/         \__\/         \__\/             '''
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
            correctGuess(guess)
        else:
            wrongGuess(guess)
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

def loserSc(gameWords):
    print(hangmanStages[7])
    print()
    print("THE WORD WAS " + gameWords + "!")

def displayLetters():
    return

def repeatGuess():
    rp = " "
    while rp != "":
        print(hangmanStages[9])
        print()
        print("YOU CANNOT GUESS A LETTER TWICE")
        print()
        rp = input("Press ENTER to continue!")
    
    
def titleScreen():
    title = " "
    while title != "":
        print(hangmanStages[10])
        print()
        title = input("Press ENTER to play!")
        
def correctGuess(guess):
    corr = " "
    while corr != "":
        print(hangmanStages[11])
        print()
        print("Your guess of letter " + guess + "was CORRECT!")
        print()
        corr = input("Press ENTER to continue!")
    
def wrongGuess(guess):
    wrg = " "
    while wrg != "":
        print(hangmanStages[12])
        print()
        print("Your guess of letter " + guess + "was WRONG!")
        print()
        wrg = input("Press ENTER to continue!")

play = True

titleScreen()

while play:
    clear()
    
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
        clear()
        
    if wrongGuesses == 6:
        loserSc(gameWord)

    print()
    print()
    ans = input("Enter 'yes' to play again, leave blank to quit:    ")
    if ans == "yes":
        wrongGuesses=0
    else:
        play = False


