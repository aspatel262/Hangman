import random

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
    '''
]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra kush ayush rupesh jaivish shivom adi heeya deeya mahitha rhea prachi vrunda krishna'.split()

#selects word write for hangman
def getWord(wordList):
    worldSelect = random.randint(0,len(wordList))
    return wordList[worldSelect]

def printHangman(wrongGuesses):
    print(hangmanStages[wrongGuesses])

play = True
win = False

while play:
    
    gameWord = getWord(words)
    
    wrongGuesses = 0
    
    while wrongGuesses < 6 and not win:
        print()
        printHangman(wrongGuesses)
        
        
        wrongGuesses+=1
        
    print("Enter yes to play again.")
    ans = input()
    if ans == "yes":
        wrongGuesses=0
    else:
        play = False


