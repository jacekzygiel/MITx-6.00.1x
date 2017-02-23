'''secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
Output: False
'''

def isWordGuessed(secretWord, lettersGuessed):
    for letter in set(secretWord):
        if letter not in lettersGuessed:
            return False 
    return True
    
