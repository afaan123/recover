"""
Problem Definition: 
•	Given 4 x 4 chessboard, arrange four queens in a way, such that no two queens attack each other. That is, no two queens are placed in the same row, column, or diagonal.
•	We have to arrange four queens, Q1, Q2, Q3 and Q4 in 4 x 4 chess board. We will put ith queen in ith row. Let us start with position (1, 1). Q1 is the only queen, so there is no issue. partial solution is <1>
•	We cannot place Q2 at positions (2, 1) or (2, 2). Position (2, 3) is acceptable. partial solution is <1, 3>.
•	Next, Q3 cannot be placed in position (3, 1) as Q1 attacks her. And it cannot be placed at (3, 2), (3, 3) or (3, 4) as Q2 attacks her. There is no way to put Q3 in third row. Hence, the algorithm backtracks and goes back to the previous solution and readjusts the position of queen Q2. Q2 is moved from positions (2, 3) to
•	(2, 4). Partial solution is <1, 4>
•	Now, Q3 can be placed at position (3, 2). Partial solution is <1, 4, 3>.
•	Queen Q4 cannot be placed anywhere in row four. So again, backtrack to the previous solution and readjust the position of Q3. Q3 cannot be placed on (3, 3) or(3, 4). So the algorithm backtracks even further.
•	All possible choices for Q2 are already explored, hence the algorithm goes back to partial solution <1> and moves the queen Q1 from (1, 1) to (1, 2). And this process continues until a solution is found.

Constraint Satisfaction Problem:
•	Next, Q3 cannot be placed in position (3, 1) as Q1 attacks her. And it cannot be placed at (3, 2), (3, 3) or (3, 4) as Q2 attacks her. 
•	There is no way to put Q3 in third row. Hence, the algorithm backtracks and goes back to the previous solution and readjusts the position of queen Q2. Q2 is moved from positions (2, 3) to (2, 4). 
•	Partial solution is <1, 4> Now, Q3 can be placed at position (3, 2). Partial solution is <1, 4, 3>.
•	Queen Q4 cannot be placed anywhere in row four. 
•	So again, backtrack to the previous solution and readjust the position of Q3. 
•	Q3 cannot be placed on (3, 3) or(3, 4). So the algorithm backtracks even further.
•	All possible choices for Q2 are already explored, hence the algorithm goes back to partial solution <1> and moves the queen Q1 from (1, 1) to (1, 2) and this process continues until a solution is found.


Complete: NO [can get stuck in loops, e.g., Complete in finite space with repeatedstate checking ]
 Time Complexity: O (bm) [but a good heuristic can give dramatic improvement]
 Space Complexity: O (bm) [keeps all nodes in memory]
Optimal: NO
Greedy best-first search is not optimal, and it is incomplete. The worst-case time and space
complexity is O (bm
), where m is the maximum depth of the search space.


"""
# Algorithm:
# ●	Create 2 empty lists: OPEN and CLOSED
# ●	Start from the initial node (say N) and put it in the ‘ordered’ OPEN list Repeat the next steps until the GOAL node is reached
# o	If the OPEN list is empty, then EXIT the loop returning ‘False’
# o	Select the first/top node (say N) in the OPEN list and move it to the CLOSED list. Also, capture the information of the parent node
# o	If N is a GOAL node, then move the node to the Closed list and exit the loop returning ‘True’. The solution can be found by backtracking the path
# o	If N is not the GOAL node, expand node N to generate the ‘immediate’ next nodes linked to node N and add all those to the OPEN list
# o	Reorder the nodes in the OPEN list in ascending order according to an evaluation function f(n).
# ●	This algorithm will traverse the shortest path first in the queue. The time complexity of the algorithm is given by O(n*logn).



import random

N = 8

def print_board_top_border():
    print("   +", end="")
    for j in range(N):
        print("---+", end="")
    print("")


def draw_board(board):
    print_board_top_border()
    for queen_row in range(len(board)):
        print(queen_row+1, " |", end="")
        queen_col = board[queen_row]
        for j in range(N):
            if j == queen_col:
                print(" Q |", end="")
            else:
                print("   |", end="")
        print("")

        print_board_top_border()

def h(input):
    count = 0
    for queen_row in range(len(input)):
        queen_col = input[queen_row]
        for queen_2_row in range(len(input)):
            queen_2_col = input[queen_2_row]

            if queen_2_row == queen_row:
                continue
            if queen_2_row - queen_2_col == queen_row - queen_col:
                # same difference, collision along NW - SE direction
                count += 1
            if queen_2_row + queen_2_col == queen_row + queen_col:
                # same sum, collision along NE - SW direction
                count += 1
    return count


def move_gen(input):
    res = []
    for i in range(1, N):
        child = input[:]
        child[0], child[i] = child[i], child[0]
        if child not in open and child not in closed:
            res.append(child)
    return res


def isSoln(board):
    # check if every queen in the board is not being attacked
    diagonal_collision = (h(board) > 0)
    two_queens_same_column = (len(set(board)) < N)
    # row collision is not possible
    return not (diagonal_collision or two_queens_same_column)

start = [0, 1, 2, 3, 4, 5, 6, 7]
start = [i for i in range(N)]
#random.shuffle(start)
open, closed = [start], []

print("\nInput: \n")
draw_board(start)

print("\nOutput: \n")

while open:
    board = open.pop(0)
    if isSoln(board):
        draw_board(board)
        break
    else:
        closed = [board] + closed
        children = move_gen(board)
        open = sorted(children + open, key=lambda x: h(x))

print("")