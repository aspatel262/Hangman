import random

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



words = {"space", "gray", "mac", "pro"}


for stage in hangmanStages:
    print(stage)
    
    print("hi")
    
    print("sending from main")
    
    #testing agian