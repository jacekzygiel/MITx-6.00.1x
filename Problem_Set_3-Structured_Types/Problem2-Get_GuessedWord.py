'''
Created on Jan 25, 2017

@author: zygielj
'''

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    return ''.join('_ ' if letter not in lettersGuessed else letter
                    for letter in secretWord)
        
print getGuessedWord(secretWord, lettersGuessed)    