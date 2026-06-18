graph = {'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}

stack = ['A']
visited = []

while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        stack.extend(graph[node])

print(visited)
