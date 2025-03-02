# 29-01-25
# write algorithm for Best first Search and A*.


#BFS
from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Use deque for efficient popping from the front

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark as visited
            queue.extend(graph[node])  # Enqueue unvisited neighbors

# Example graph (Adjacency List)
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

# Call BFS
print("BFS Traversal:")
bfs(graph, 'A')


##############################################################

# A* algorithm
import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue to store (f_score, node, path, g_score)
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], start, [start], 0))

    # Dictionary to track the lowest cost to reach a node
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0

    while open_list:
        # Get the node with the lowest f-score
        f_score, current, path, g_score = heapq.heappop(open_list)

        # If we reach the goal, return the path
        if current == goal:
            return path, g_score

        # Explore neighbors
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score + cost  # Calculate new g-score
            
            # If a shorter path to neighbor is found, update
            if tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor, path + [neighbor], tentative_g_score))

    return None  # No path found

# Example Graph (Adjacency List with Costs)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('E', 1)],
    'E': [('B', 5), ('D', 1), ('F', 2)],
    'F': [('C', 3), ('E', 2)]
}

# Heuristic Values (Estimated cost to reach goal 'F')
heuristic = {
    'A': 6, 'B': 4, 'C': 2, 'D': 3, 'E': 1, 'F': 0
}

# Run A* Algorithm
start_node = 'A'
goal_node = 'F'
path, cost = a_star(graph, start_node, goal_node, heuristic)

print(f"Shortest Path: {path}")
print(f"Total Cost: {cost}")
