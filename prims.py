
def prims(n):
    INF = 9999999
    # number of vertices in graph
    N = 5
    #creating graph by adjacency matrix method
    G = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]

    selected_node = [0, 0, 0, 0, 0]

    no_edge = 0

    selected_node[n] = True

    # printing for edge and weight
    print("Edge : Weight\n")
    while (no_edge < N - 1):
        
        minimum = INF
        a = 0
        b = 0
        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if ((not selected_node[n]) and G[m][n]):  
                        # not in selected and there is an edge
                        if minimum > G[m][n]:
                            minimum = G[m][n]
                            a = m
                            b = n
        print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
        selected_node[b] = True
        no_edge += 1
def menu():
    n=int(input('enter'))
    prims(n)
menu()
