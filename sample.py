class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []
        

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            print("-----")
            print(parent)
           
            print(rank)
            print("-----")
		
        while e < self.V - 1:
            print("####")
            print(parent)
            print(rank)
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            print(x)
            y = self.find(parent, v)
            print(y)

            if x != y:
                e += 1
                result.append([u, v, w])
                print(result)
                self.union(parent, rank, x, y)

        # Print the minimum spanning tree
        print("Minimum Spanning Tree:")
        for u, v, weight in result:
            print(f"{u} -- {v} \tWeight: {weight}")


# Example usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal()
