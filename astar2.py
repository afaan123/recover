"""
A* Search Algorithm:
•	A* Search Algorithm is a simple and efficient search algorithm that can be used to find the optimal path between two nodes in a graph. 
•	It will be used for the shortest path finding, it is an extension of Dijkstra’s shortest path algorithm (Dijkstra’s Algorithm). 
•	The extension here is that, instead of using a priority queue to store all the elements, we use heaps (binary trees) to store them. 
•	The A* Search Algorithm also uses a heuristic function that provides additional information regarding how far away from the goal node we are, this function is used in conjunction with the f-heap data structure in order to make searching more efficient.
•	In the event that we have a grid with many obstacles and we want to get somewhere as rapidly as possible, the A* Search Algorithms are our saviour. 
•	From a given starting cell, we can get to the target cell as quickly as possible , it is the sum of two variables’ values that determines the node it picks at any point in time. 
•	At each step, it picks the node with the smallest value of ‘f’ (the sum of ‘g’ and ‘h’) and processes that node/cell. 
                 f(n) = g(n) + h(n)
•	‘g’ and ‘h’ is defined as simply as possible below:
o	‘g’ is the distance it takes to get to a certain square on the grid from the starting point, following the path we generated to get there. 
o	‘h’ is the heuristic, which is the estimation of the distance it takes to get to the finish line from that square on the grid


Algorithm (A*):
open = list(start)
f(start) = h(start)
parent(start) = nil
closed = ()
while open not empty do
	Remove a node 'n' from open such that f(n) has the lowest value
	Add 'n' to closed
	if GoalTest(n) == True then return ReConstructPath(n)
	neighbours = MoveGen(n)
	for each m ∈ neighbours do
		if m is not in open and m is not in closed then
			Add 'm' to open
			parent(m) = n
			g(m) = g(n) + k(n, m)
			f(m) = g(m) + h(m)
		else if m is in open then
			if(g(n)+k(n, m)<g(m)) then
				parent(m) = n
				g(m) = g(n) + k(n, m)
				f(m) = g(m) + h(m)
		else if m is in closed then
			if(g(n)+k(n, m)<g(m)) then
				parent(m) = n
				g(m) = g(n) + k(n, m)
				f(m) = g(m) + h(m)
				PropagateImprovement(m)






"""


INFINITY = 999999

def remove_seen(children, open, closed):
    open_heads_list = [i[0] for i in open]
    closed_heads_list = [i[0] for i in closed]
    return [i for i in children if i not in open_heads_list + closed_heads_list]


def find_link(node, closed_list):
    for i in closed_list:
        if i[0] == node:
            return i


def reconstruct_path(nodepair, closed_list):
    node, parent, *a = nodepair
    result = [node]
    while parent is not None:
        node, parent, *_ = find_link(parent, closed_list)
        result.append(node)
    result.reverse()
    return result


def moveGen(node):
    res = []
    for neighbour in range(n):
        if cost[node[0]][neighbour] != INFINITY:
            # there is an edge between that node to neighbour
            w = cost[node[0]][neighbour]
            g = node[2] + w
            res.append((
                neighbour,
                node[0],
                g,
                h[neighbour],
                g + h[neighbour]
            ))
    
    return res


def compute_cost(path):
    res = 0
    for i in range(len(path)-1):
        res += cost[path[i]][path[i+1]]
    return res


nodesList = input('Enter Node Names (e.g "A B C D"): ').strip().split(" ")
n = len(nodesList)

h = []
for node in nodesList:
    h.append(int(input("Enter heuristic value for " + node + ": ")))

cost = [[INFINITY for i in range(n)] for j in range(n)]

print('Enter Edges: ')
print('Note: Enter edge as end,end,end to stop entering more edges\nEnter Node names in Capital Letters')
print('')
count = 0
while True:
    count += 1
    print("Enter Edge", count, ":")
    u, v, w = input("Enter source, destination and weight as u, v, w (eg. A, B, 2): ").strip().split(" ")
    if u == "end" or v == "end":
        break
    w = int(w)
    cost[nodesList.index(u)][nodesList.index(v)] = w
    cost[nodesList.index(v)][nodesList.index(u)] = w

print("")

source = nodesList.index(input("Enter source node: "))
goal = nodesList.index(input("Enter dest node: "))

# main A* logic
open = [(source, None, 0, h[0], 0+h[0])]
closed = []
while open:
    node = open.pop(0)
    if node[0] == goal:
        path = reconstruct_path(node, closed)
        print("Path: ",end='')
        print(*[nodesList[i] for i in path], sep=" -> ")
        print("Cost of this path is:", compute_cost(path))
        break
    else:
        closed.append(node)
        children = moveGen(node)
        noLoops = remove_seen(children, open, closed)
        open = sorted(children + open, key=lambda x: x[-1])