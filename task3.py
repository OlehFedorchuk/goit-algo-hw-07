class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sum_tree(root):
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)

# Створимо дерево вручну
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)

print("Сума всіх значень у дереві:", sum_tree(root))
# Виведе: Сума всіх значень у дереві: 45