def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    def isHandValid(word, hand):
        string = hand.copy()
        result = None
        for char in word:
            if char not in string or string[char] == 0:
                return False
            else:
                result = True
                string[char] -= 1
        return result

    while isHandValid(word,hand):
        if word in wordList:
            return True
        else:
            return False
    return False

    
                
                
            
            
        


#Testing

print(isValidWord('chayote', {'a': 1, 'h': 1, 'o': 2, 'y': 1, 'c': 2, 'u': 2, 'z': 1, 't': 2},'chayote'))


