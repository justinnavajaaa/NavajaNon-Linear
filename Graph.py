
from collections import deque



graph = {
    "N": ["A1", "V"],
    "A1": ["N", "A2", "J"],
    "V": ["N", "A3"],
    "A2": ["A1"],
    "J": ["A1"],
    "A3": ["V"]
}



def display_name(node):
    if node.startswith("A"):
        return "A"
    return node



def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while queue:
        current = queue.popleft()
        result.append(display_name(current))

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result



def dfs(graph, start):
    visited = set()
    result = []

    def traverse(node):
        visited.add(node)
        result.append(display_name(node))

        for neighbor in graph[node]:
            if neighbor not in visited:
                traverse(neighbor)

    traverse(start)
    return result


# 5. Display Results
print("====================================")
print("           NAVAJA GRAPH")
print("====================================")

print("\nGraph Connections:")

for node, neighbors in graph.items():
    print(f"{node}: {', '.join(neighbors)}")

print("\nBFS (Breadth-First Search):")
print(" -> ".join(bfs(graph, "N")))

print("\nDFS (Depth-First Search):")
print(" -> ".join(dfs(graph, "N")))

print("\n====================================")
print("Program completed successfully!")
