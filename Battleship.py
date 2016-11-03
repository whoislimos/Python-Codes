from random import randint

board = []

# System creates a 5 x 5 board
for x in range(5):
    board.append(["O"] * 5)


# Show user the battleship board
def print_board(board):
    for row in board:
        print " ".join(row)


print "Let's play Battleship!"
print " -> Remember, you only have 4 turns!"
print "------------------------------------ "
print_board(board)

def random_row(board):
    return randint(1, len(board) )

def random_col(board):
    return randint(1, len(board) )

ship_row = random_row(board)
ship_col = random_col(board)


# Debugging Only - Show the actual location of the battleship
print " "
print "Actual Ship Row Location :" , ship_row
print "Actual Ship Column Location: " , ship_col
print " "


# User has a maximum of four turns at guessing
for turn in range(4):
    print "Turn", turn + 1
    
    # User guess the position of battleship
    guess_row = int(raw_input("Guess Row (Between 1 and 5):"))
    guess_col = int(raw_input("Guess Col (Between 1 and 5):"))
    print "------------------------------ "
    
    
    # Conditions for guessing correctly or incorrectly
    if guess_row == ship_row and guess_col == ship_col:
        print "CONGRATULATIONS! You sunk my battleship!"
        break
    else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row - 1][guess_col - 1] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row - 1][guess_col - 1] = "X"
                        
        if turn == 3:
            print "Game Over"
        print " "
        print_board(board)
        print " "
        
        
        
        
