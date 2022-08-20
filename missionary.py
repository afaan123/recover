"""Algorithm:
1. Create a variable called NODE-LIST and set it to initial state
2. Until a goal state is found or NODE-LIST is empty do
a. Remove the first element from NODE-LIST and call it E. If NODE-LIST was empty,
quit
b. For each way that each rule can match the state described in E do:
i. Apply the rule to generate a new state
ii. If the new state is a goal state, quit and return this state
iii. Otherwise, add the new state to the end of NODE-LIST

Breadth first search is:
 One of the simplest search strategies
 Complete. If there is a solution, BFS is guaranteed to find it.
 If there are multiple solutions, then a minimal solution will be found
 The algorithm is optimal (i.e., admissible) if all operators have the same cost. Otherwise,
breadth first search finds a solution with the shortest path length.
 Time complexity : O(bd
)
 Space complexity : O(bd
)
 Optimality :Yes
b - branching factor(maximum no of successors of any node),
d – Depth of the shallowest goal node
Maximum length of any path (m) in search space

Advantages: Finds the path of minimal length to the goal.
Disadvantages:
 Requires the generation and storage of a tree whose size is exponential the depth of the
shallowest goal node.
 The breadth first search algorithm cannot be effectively used unless the search space is quite
small.
"""

#One of the many ways to represent the state space is as follows.
#L(M1,C1)&&R(M2, C2)&&(BL || BR) where 
#(M1 >= C1 || M1 =0), 
#(M2 >= C2 || M2 =0), 
#M1 + M2 = 3, M1, M2 Œ (0, 3)
#C1 + C2 = 3,C1, C2 Œ (0, 3) 



def is_state_valid(curr_state):
    """check if a given state is valid or not."""
    M, C, B = curr_state

    if 0 <= M <= 3 and 0 <= C <= 3 and (M == 0 or M >= C) and (3 - M == 0 or 3 - M >= 3 - C):
        return True
    return False


def move_gen(nodepair):
    """generate the next possible moves from a given state"""
    M, C, B, path = nodepair
    
    # eg (2, 2, True)
    # we can:
    #       send 2 M on right, 
    #       ∴ (0, 2, False)
    #       send 2 C on right, 
    #       ∴ (2, 0, False)
    #       send 1 M and 1 C on right, 
    #       ∴ (1, 1, False)
    #       send 1 C on right, 
    #       ∴ (2, 1, False)
    #       send 1 M on right, 
    #       ∴ (1, 2, False)
    # of these, we use is_state_valid function, to remove invalid states
    # Hence, (2, 0, False), (2, 1, False) and (1, 2, False) will be removed
    # ∴ valid_states = [(0, 2, False), (1, 1, False)]

    moves = [[1, 1],[1, 0],[0, 1],[0, 2],[2, 0]]
    valid_states = []
    for each in moves:
        if(B == False):
            next_state = [M + each[0], C + each[1], True, path + [(M, C, B)]]
        else:
            next_state = [M - each[0], C - each[1], False, path + [(M, C, B)]]

        if (is_state_valid(next_state[:3])):
            valid_states.append(next_state)

    return valid_states


def goal_test(current_state):
    M, C, B = current_state
    return M == 0 and C == 0



start = [3, 3, True, []]
open = [start]
visited = []

while open:
    curr_state = open.pop(0)
    if curr_state not in visited:
        visited.append(curr_state[:3])
    if goal_test(curr_state[:3]):
        curr_state[-1] += [[0, 0, False]]
        print("Solution Found!", curr_state[-1])
    else:
        new_states = move_gen(curr_state)
        for state in new_states:
            if state[:3] not in visited and is_state_valid(state[:3]):
               open.append(state)    #BFS
               # open=[state]+open   #DFS