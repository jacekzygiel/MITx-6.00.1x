from ps4a import getFrequencyDict

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    freqDict = getFrequencyDict(word)
    hand = hand.copy()
    if word in wordList:
        for letter in word:
            if hand[letter] in freqDict[word]:
                return True
    return False
            
            
            