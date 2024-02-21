from collections import deque


def bfs (graph,start) :
    
    visited = set()
    queue = deque([start])
    
    while queue :
        vertex = queue.popleft()
        if vertex not in visited : 
            visited.add(vertex)
            print(vertex , end="")
            
            queue.extend( neighbour for neighbour in graph[vertex] if neighbour not in visited)
        
    

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

bfs(graph,'A')



