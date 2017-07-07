def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    def showHand(hand):
      string = ''
      for i in hand.keys():
            
            for j in range(hand[i]):
                  string += str(i + ' ' )
      return string

    handLength = calculateHandlen(hand)
    gameOver = False
    currPoints = 0
    string = hand.copy()
    while gameOver == False:

        
        if showHand(string) == '':
            print('Run out of letters. Total score: ' + str(currPoints))
            gameOver = True
            break
        
        print('Current Hand: ' + showHand(string))
        userInput = input('Enter word, or a "." to indicate that you are finished: ')
        validWord = isValidWord(userInput, string, wordList)
        if userInput == '.':
            print('Goodbye! Total score: ' + str(currPoints) + ' points.')
            gameOver = True
            break

        
            
        elif userInput not in wordList or validWord == False:
            print('Invalid word, please try again.')
            print('')

        else:          
            wordPoints = getWordScore(userInput, handLength)
            currPoints += wordPoints
            print(str(userInput) + ' earned ' + str(wordPoints) + ' points. Total: ' + str(currPoints) + ' points')
            print('')

            string = updateHand(string, userInput)
