def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    word=secretWord
    print('Welcome to the game, Hangman!\nI am thinking of a word that is '+str(len(word))+ ' letters long''\n------------')
    #-------------------------------------------------------------------------------------------------------------
    guesses=8
    guesslist=[]
    finalword=''.join(guesslist)
    while guesses!=-1:
        if getGuessedWord(secretWord, guesslist)==secretWord:
                          print('Congratulations, you won!')
                          break
        elif guesses==0:
            print('Sorry, you ran out of guesses. The word was ' + str(secretWord))
            break
        else:
            print('You have '+str(guesses)+' left.')
            print('Available letters: '+ str(getAvailableLetters(guesslist)))
            lettersGuessed=input('Please guess a letter:').lower()
            
            if lettersGuessed in word:
                if lettersGuessed in guesslist:
                        print("Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, guesslist))+'\n------------')
                elif lettersGuessed not in guesslist:
                    if lettersGuessed in word:
                        guesslist.append(lettersGuessed)
                        print('Good guess:'+ str(getGuessedWord(secretWord, guesslist))+'\n------------')
                        getGuessedWord(secretWord, guesslist)
           
            elif lettersGuessed not in secretWord:
                if lettersGuessed in guesslist:
                    print("Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, guesslist))+'\n------------')
                elif lettersGuessed not in guesslist:
                    guesses-=1
                    guesslist.append(lettersGuessed)
                    print('Oops! That letter is not in my word: '+ str(getGuessedWord(secretWord, guesslist))+'\n------------')
                    getGuessedWord(secretWord, guesslist)
