"""Algorithm:
1. Create a variable called NODE-LIST and set it to initial state
2. Until a goal state is found or NODE-LIST is empty do
a. Remove the first element from NODE-LIST and call it E. If NODE-LIST was empty,
quit
b. For each way that each rule can match the state described in E do:
i. Apply the rule to generate a new state
ii. If the new state is a goal state, quit and return this state
iii. Otherwise, add the new state in front of NODE-LIST

Depth first searchis:
1. The algorithm takes exponential time.
2. If N is the maximum depth of a node in the search space, in the worst case the algorithm will
take time O(b
d
).
3. The space taken is linear in the depth of the search tree, O(bN). 



1.	(x,y)	If x<4	(4,y)	Fill the 4 gallon jug completely
2.	(x,y)	if y<3	(x,3)	Fill the 3-gallon jug completely
3.	(x,y)	If x>0	(x-d,y)	Pour some part from the 4 gallon jug
4.	(x,y)	If y>0	(x,y-d)	Pour some part from the 3 gallon jug
5.	(x,y)	If x>0	(0,y)	Empty the 4 gallon jug
6.	(x,y)	If y>0	(x,0)	Empty the 3 gallon jug
7.	(x,y)	If (x+y)<7	(4, y-[4-x])	Pour some water from the 3 gallon jug to fill the four gallon jug
8.	(x,y)	If (x+y)<7	(x-[3-y],y)	Pour some water from the 4 gallon jug to fill the 3 gallon jug.
9.	(x,y)	If (x+y)<4	(x+y,0)	Pour all water from 3 gallon jug to the 4 gallon jug
10.	(x,y)	if (x+y)<3	(0, x+y)	Pour all water from the 4 gallon jug to the 3 gallon jug

"""
def move_gen(node):
    result = []
    x, y = node
    dx, dy = A - x, B - y
    if x < A:
        # fill in Jug A, if it's not full
        result.append((A, y))
    if y < B:
        # fill in Jug B, if it's not full
        result.append((x, B))
    if x > 0:
        # empty Jug A, if it's not empty
        result.append((0, y))
    if y > 0:
        # empty Jug B, if it's not empty
        result.append((x, 0))
    if x > 0 and x + y <= B:
        # if water in jug A can be poured in jug B without overflowing B, do that
        result.append((0, x + y))
    if x > 0 and x + y > B:
        # if water in jug A can't be poured in jug B without overflowing B, pour water from A until B is full. Some water will be left in jug A
        result.append((x - dy, B))
    if y > 0 and y + x <= A:
        # if water in jug B can be poured in jug A without overflowing A, do that
        result.append((x + y, 0))
    if y > 0 and y + x > A:
        # if water in jug B can't be poured in jug A without overflowing A, pour water from B until A is full. Some water will be left in jug B
        result.append((A, y - dx))

    return result


def remove_seen(children, open_list, closed_list):
    open_heads_list = [i[0] for i in open_list]
    closed_heads_list = [i[0] for i in closed_list]
    return [i for i in children if i not in open_heads_list + closed_heads_list]


def make_pairs(children_list, parent):
    return [(child, parent) for child in children_list]


def find_link(node, closed_list):
    return list(filter(lambda x: x[0] == node, closed_list))[0]


def reconstruct_path(nodepair, closed_list):
    node, parent = nodepair
    result = [node]
    while parent is not None:
        node, parent = find_link(parent, closed_list)
        result.append(node)
    result.reverse()
    return result

if __name__ == '__main__':
    A, B = 4, 3
    start = (0, 0)
    goal = (2, 0)
    open = [(start, None)]
    closed = []
    while open:
        nodepair = open.pop(0)
        node = nodepair[0]
        if node == goal:
            print("Goal state can be reached through path:\n", *reconstruct_path(nodepair, closed))
            
        else:
            closed = [nodepair] + closed
            children = move_gen(node)
            noLoops = remove_seen(children, open, closed)
            new = make_pairs(noLoops, node)
            open = new + open       #DFS
            #open = open + new       # BFS