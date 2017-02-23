from string import ascii_lowercase
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):    
    return ''.join(letter if letter not in lettersGuessed else ''
                   for letter in ascii_lowercase)

print getAvailableLetters(lettersGuessed)            