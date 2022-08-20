"""Problem Definition: 
•	We also know the eight puzzle problem by the name of N puzzle problem or sliding puzzle problem.
•	N-puzzle that consists of N tiles (N+1 titles with an empty tile) where N can be 8, 15, 24 and so on.
•	In our example N = 8. (that is square root of  (8+1) = 3 rows and 3 columns).
•	In the same way, if we have N = 15, 24 in this way, then they have Row and columns as follow (square root of (N+1) rows  and square root of (N+1) columns).
•	That is if N=15 than number of rows and columns= 4, and if N= 24 number of rows and columns= 5.
•	So, basically in these types of problems we have given a initial state or initial configuration (Start state) and a Goal state or Goal Configuration.
•	Here We are solving a problem of 8 puzzle that is a 3x3 matrix.



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



def remove_seen(children, open_list, closed_list):
    # print(children)
    open_heads_list = [i[0] for i in open_list]
    closed_heads_list = [i[0] for i in closed_list]
    return [i for i in children if i not in open_heads_list + closed_heads_list]


def make_pairs(children_list, parent):
    return [(child, h(child), parent) for child in children_list]


def find_link(node, closed_list):
    for i in closed_list:
        if i[0] == node:
            return i


def reconstruct_path(nodepair, closed_list):
    node  = nodepair[0]
    parent = nodepair[-1]
    result = [node]
    while parent is not None:
        node = find_link(parent, closed_list)[0]
        parent = find_link(parent, closed_list)[-1]
        result.append(node)
    result.reverse()
    return result


def find_tile(board, tile):
    for i in range(3):
        for j in range(3):
            if board[i][j] == tile:
                return (i, j)


def h(board):
    res = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != -1:
                goal_i, goal_j = find_tile(goal, board[i][j])
                res += (abs(i - goal_i) + abs(j - goal_j))
    return res


def copy(board):
    l = []
    for i in board:
        l.append(i[:])
    return l

def move_gen(current_board):
    result = []
    empty_x, empty_y = find_tile(current_board, -1)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        board_copy = copy(current_board)
        if 0 <= empty_x + dx < 3 and 0 <= empty_y + dy < 3:
            board_copy[empty_x][empty_y], board_copy[empty_x+dx][empty_y+dy] = board_copy[empty_x+dx][empty_y+dy], board_copy[empty_x][empty_y]
            result.append(board_copy)

    return result


# state representation
"""start = [
    [5,  8,  6],
    [7,  2,  4],
    [3, -1,  1]
]
goal = [
    [1,  2,  3],
    [4, -1,  5],
    [6,  7,  8]
]
"""

start = [[1,2,3],[7,8,4],[6,-1,5]]
goal=[[1,2,3],[8,-1,4],[7,6,5]]


solutionExists = False
open = [(start, h(start), None)]
closed = []

while open:
    nodepair = open.pop(0)
    node = nodepair[0]
    if node == goal:
        print("Goal state can be reached through path:", *reconstruct_path(nodepair, closed))
        solutionExists = True
        break
    else:
        closed = [nodepair] + closed
        children = move_gen(node)
        noLoops = remove_seen(children, open, closed)
        new = make_pairs(noLoops, node)
        open = sorted(new + open , key=lambda x:x[1])     # Best First Search


if not solutionExists:
    print("No solution")
