"""
Theory:
•	Tic Tac Toe is one of the most played games and is the best time killer game that you can play anywhere with just a pen and paper.
•	If you don’t know how to play this game don’t worry let us first understand that.
•	The game is played by two individuals and first, we draw a board with a 3×3 square grid. 
•	The first player chooses ‘X’ and draws it on any of the square grid, then it’s the chance of the second player to draw ‘O’ on the available spaces. 
•	Like this, the players draw ‘X’ and ‘O’ alternatively on the empty spaces until a player succeeds in drawing 3 consecutive marks either in the horizontal, vertical or diagonal way. 
•	Then the player wins the game otherwise the game draws when all spots are filled.


Rules Of Tic Tac Toe Problem: 
•	Traditionally the first player plays with "X". So you can decide who wants to go with "X" and who wants to go with "O".
•	Only one player can play at a time.
•	If any of the players have filled a square then the other player and the same player cannot override that square.
•	There are only two conditions that may match will be draw or may win.
•	The player that succeeds in placing three respective marks (X or O) in a horizontal, vertical, or diagonal row wins the game.



MINMAX ALGORITHM
/* TO return the minmax value V(j) of a node j*/
if Terminal(j)
    then return V(j) <- e(j)
    else for i<- 1 to b  /* b is the branching factor */
           do
             Generate j the i'th successor of j
             V(ji) <- Minimax(ji)  /*recursive call8?
             if i= 1
                then CV(j) <- V(ji)
                else if j is MAX
                        then CV(j) <- Max(CV(j), V(ji))
                        else CV(j) <- Min(CV(j), V(ji))
return V(j) <- CV(j)
"""
"""
BESTMOVE(j)
    /* To return the best successor b of a node j */
    b <- NIL
    value <- -Large
    for i <- 1 to b
        do V(ji) <- Minimax(ji)
        if V(ji) > value
            then value <- V(ji)
                    b<- ji
return b
"""


maxPlayer, minPlayer = 'x', 'o'

def evaluate(board):
    if all([board[i][j] == ' ' for i in range(3) for j in range(3)]):
        # if all the places 
        return 0

    if ['x']*3 in board:
        return 10

    if ['o']*3 in board:
        return -10
    
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[1][col] != ' ':
            return 10 if board[1][col] == 'x' else -10
    
    if len(set([board[i][i] for i in range(3)])) == 1 and board[1][1] != ' ':
        return 10 if board[1][1] == 'x' else -10
    
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[1][1] != ' ':
        return 10 if board[1][1] == 'x' else -10
    
    return 0


def game_over(board):
    if(evaluate(board) == 10 or evaluate(board)  == -10):
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False

    return True


def minimax(board, depth, isMax):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score
    
    if game_over(board):
        return 0
    
    if isMax:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = maxPlayer
                    best_score = max(best_score, minimax(board, depth+1, not isMax))
                    board[i][j] = ' '
        return best_score
    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = minPlayer
                    best_score = min(best_score, minimax(board, depth+1, not isMax))
                    board[i][j] = ' '
        return best_score


def findBestMove(board, isMax):
    bestVal = -1000 if isMax else 1000
    # bestVal = -1000, if X's turn (max player) else it is Y's turn
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                board[i][j] = maxPlayer if isMax else minPlayer

                moveVal = minimax(board, 0, not isMax)

                board[i][j] = ' '

                if (isMax and moveVal > bestVal) or (not isMax and moveVal < bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal
    
    return bestMove


def printBoard(board):
    print()
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(f" {board[i][j]} ")
            else:
                print(f" {board[i][j]} ", end='|')
        if i != 2:
            print("---+---+---")
    print()


if __name__ == "__main__":
    board = [
        [ ' ', ' ', ' ' ],
        [ ' ', ' ', ' ' ],
        [ ' ', ' ', ' ' ]
    ]
    printBoard(board)
    print("Hello User! Welcome")

    choice = -1
    while choice not in ['x', 'o']:
        print("Play as [x/o]: ", end='')
        choice = input().strip()
    if choice == 'x':
        user, pc = 'x', 'o'
        isMax = False
    else:
        user, pc = 'o', 'x'
        isMax = True

    
    choice = -1
    while choice not in ['y', 'n']:
        print("Do you want to make first move? [y/n]: ", end='')
        choice = input().strip()

    turn = "user"
    if choice == 'n':
        board[0][0] = pc
        printBoard(board)
        turn = "user"
    

    while not game_over(board):
        if turn == "user":
            while True:
                print("Enter position to place", user)
                position_x, position_y = map(int, input().strip().split(" "))
                if (position_x, position_y) != (-1, -1) and board[position_x][position_y] == ' ':
                    break
                print("The position is already occupied")
            board[position_x][position_y] = user
        else:
            bestMove = findBestMove(board, isMax)
            board[bestMove[0]][bestMove[1]] = pc
        
        turn = "user" if turn == "pc" else "pc"
        printBoard(board)
    
    if(evaluate(board) == 10 or evaluate(board)  == -10):
        print("x won" if evaluate(board) == 10 else "y won")
    else:
        print("Game drawn!")
