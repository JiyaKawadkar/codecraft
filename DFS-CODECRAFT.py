def dfs(graph, start):
   

    visited = set()  
    stack = [start] 
    while stack:
        vertex = stack.pop()  
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]) 

    return visited
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_vertex = 'A'
visited_vertices = dfs(graph, start_vertex)
print(visited_vertices) 