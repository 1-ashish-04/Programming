

node = int(input("Enter number of nodes: "))

graph = []

for i in range(node):
    graph.append([0]*node)

for i in graph:
    print(i)
print("")

edge = int(input("Enter number of edges in a graph: "))

for i in range(edge):
    print(f"Enter below the nodes which need to connec though an {i+1} edge")
    n1 = int(input("Enter node 1: "))
    n2 = int(input("Enter node 2: "))
    graph[n1-1][n2-1] = 1
    graph[n2-1][n1-1] = 1

for i in graph:
    print(i)
