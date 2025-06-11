class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min_value(root):
    if root is None:
        return None
    
    current = root
    while current.left is not None:
        current = current.left
    return current.key

# Створимо приклад дерева вручну
root = Node(25)
root.left = Node(15)
root.right = Node(35)
root.left.left = Node(5)
root.left.left.left = Node(2)

print("Найменше значення в дереві:", find_min_value(root))
# Виведе: Найменше значення в дереві: 2