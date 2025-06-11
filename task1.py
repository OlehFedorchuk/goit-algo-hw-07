class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max_value(root):
    if root is None:
        return None
    
    current = root
    while current.right is not None:
        current = current.right
    return current.key

# Створимо просте дерево вручну
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.right = Node(40)
root.right.right.right = Node(50)

print("Найбільше значення в дереві:", find_max_value(root))
# Виведе: Найбільше значення в дереві: 50