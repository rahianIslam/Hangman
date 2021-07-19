def hangman(word):
    wrong = 0
    
    stages = [
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    nletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    print("\n")
    while wrong < len(stages)-1:
        
        start = input("Guess a letter: ")
        if start == word:
            print(" \nYou win!")
            print(start)
            print("\n".join(stages[: wrong]))
            win = True
            break


        elif start in nletters:
            
            letterPos = nletters.index(start) 
            board[letterPos] = start
            print(" ".join(board))

        else:
            wrong += 1
            print(" ".join(board))
            print("\n".join(stages[: wrong]))

        if '_' not in board:
            print("You win")
            print(" ".join(board))
            print("\n".join(stages[: wrong]))
            win = True
            break
    if not win:
        
        print(" ".join(board))
        print("\n You lose! The word is {}".format(word) )
        print("\n".join(stages[: wrong]))

            


hangman('catman')


        


