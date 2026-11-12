
from collections import deque



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



root = Node("N")

root.left = Node("A")
root.right = Node("V")

root.left.left = Node("A")
root.left.right = Node("J")

root.right.left = Node("A")


def bfs(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result



def dfs(root):
    result = []

    def traverse(node):
        if node is None:
            return

        result.append(node.data)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return result


print("====================================")
print("       NAVAJA BINARY TREE")
print("====================================")

print("\nBinary Tree Structure:")
print("          N")
print("        /   \\")
print("       A     V")
print("      / \\   /")
print("     A   J A")

print("\nBFS (Breadth-First Search):")
print(" -> ".join(bfs(root)))

print("\nDFS (Depth-First Search):")
print(" -> ".join(dfs(root)))

print("\n====================================")
print("Program completed successfully!")
