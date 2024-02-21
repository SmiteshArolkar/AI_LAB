from collections import deque

def dfs(graph , start , visited = None) : 
    if visited is None :
        visited = set()
    
    if start not in visited :
        print(start,end="")
        visited.add(start)
        
        for neighbour  in graph[start] : 
            dfs(graph,neighbour,visited)
            
            
            
            
def dfs_stack(graph,start) : 
    visited = set()
    
    stack = [start]
    
    while stack : 
        vertex = stack.pop()
        
        if vertex not in visited : 
            print(vertex,end="")
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
           



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

print("DFS starting from vertex 'A':")
dfs(graph, 'A')
print("\n")
dfs_stack(graph,'A')
