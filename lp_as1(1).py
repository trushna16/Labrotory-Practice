import json
visited=[]
def input1():
	fp = open('graph.txt')
	graph1= fp.read()
	graph2 = json.loads(graph1)
	
	#graph2 = {int(k):v for k,v in graph2.items()}
	print(graph2)
	return graph2

def DFS(node,graph):
	
	visited.append(node)
	
	for child in graph[node]:
		if child not in visited:
			DFS(child,graph)
			
	return visited
def BFS(node, gvisitedraph):
	visited=[]
	queue=[]
	
	visited.append(node)
	queue.append(node)
	
	while queue:
		m = queue.pop(0)
	
		for child in gvisitedraph[m]:
			if child not in visited:		
				visited.append(child)	
				queue.append(child)
	return visited
					
	

def menu():
	flag = True
	while(flag):
		visited.clear()
		print("1] DFS\n 2] BFS\n 3] exit")
		choice= input("Enter choice: ")
		node= input("Enter the starting node: ")
		if choice=='1':
			print("Graph sequence DFS: ",DFS(node,graph))
		elif choice=='2':
			print("Graph sequence BFS: ",BFS(node,graph))
		elif choice=='3':
			flag = False

			
	
graph = input1()
menu()


