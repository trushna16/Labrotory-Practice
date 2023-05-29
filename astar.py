def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contains an adjacency map of all nodes m
    # ditance of starting node from itself is zero
    g[start_node] = 0  # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None  # node with Lowest f( ) is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            break
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n
                        # if m in closed set, remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        # remove n from the open_set and add it to closed_set
        # because all of its neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)

    if n == None:
        print('Path does not exist!')
        return None

    # reconstruct the path from the start_node to n
    path = []
    while parents[n] != n:
        path.append(n)
        n = parents[n]
    path.append(start_node)
    path.reverse()
    print(f'Path found: {path}')
    return path


# define function to return neighbor and its distance
# from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


# for simplicity we'll consider heuristic distances given
# and this function returns heuristic distance for all nodes
def heuristic(n):
    H_dist = {
        'Maharashtra': 11,
        'Gujrat': 6,
        'Rajsthan': 99,
        'UP': 1,
        'Kerla': 7,
        'Tamil_Nadu': 0
    }
    return H_dist[n]


# Describe your graph here
Graph_nodes = {'Maharashtra': [('Gujrat', 2), ('Kerla', 3)],
               'Gujrat': [('Rajsthan', 1), ('UP', 9)],
               'Rajsthan': None,
               'Kerla': [('Tamil_Nadu', 6)],
               'Tamil_Nadu': [('UP', 1)],
               'UP': None,
               }

flag = True
while(flag):
	print(" Maharashtra\tGujrat\nKerla\tRajsthan\nUP\tTamil_Nadu\n")
	start = input("Start Node: ")
	goal = input("Goal Node: ")
	aStarAlgo(start,goal)
	ans = input("Continue?(y/n): ")
	if(ans=='n'):
	    flag = False