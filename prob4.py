def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    result = 0
    for i in hand:
        result += hand[i]
    return result
        
        


#Testing

x = {'a': 1, 'h': 1, 'o': 2, 'y': 1, 'c': 2, 'u': 2, 'z': 1, 't': 2}

print(calculateHandlen(x))
