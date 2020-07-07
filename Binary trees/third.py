import numpy as np
import timeit

arc = np.array([81, 77, 79, 68, 10, 12, 13, 20, 15, 24, 27, 42, 33, 51, 57])
darc = -np.sort(-arc)
x = (len(darc)) - 1
bark = 0
for i in range(len(darc)):
    bark = int(darc[i]) + bark
bark = bark / x
print(bark)


class Node(object):
    def __repr__(self):
        return f"Это объект с ключом {self.root}"

    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def printTree(start, traver):
    if start:
        traver = traver + (str(start.root)) + " - "
        traver = printTree(start.left, traver)
        traver = printTree(start.right, traver)
    return traver


class Binary_Tree(object):
    def __init__(self, root):
        self.root = Node(root)


def poisk(start, value):
    if start:
        if start.root == value:
            print(f"Ваше значение найдено!")
            return True
        else:
            poisk(start.left, value)
            poisk(start.right, value)

def poisk_2(arc, value):
    if value in arc:
        print(f"Ваше значение найдено!")
        return True
    return False


tree = Binary_Tree(darc[0])
tree.root.right = Node(79)
tree.root.right.right = Node(77)
tree.root.right.left = Node(68)
tree.root.right.right.left = Node(57)
tree.root.right.right.left = Node(51)
tree.root.left = Node(42)
tree.root.left.left = Node(33)
tree.root.left.right = Node(27)
tree.root.left.left.right = Node(24)
tree.root.left.left.left = Node(20)
tree.root.left.right.left = Node(15)
tree.root.left.right.right = Node(13)
tree.root.left.right.left.left = Node(12)
tree.root.left.right.left.left = Node(10)

print("массив")
print(darc)
print("дерево")
a = printTree(tree.root, " ")
print(a)
print("\nsecond task")
x = int(input("Введите значение, которе надо будет искать в списках >>> \n"))


print("поиск через массив")
b = timeit.default_timer()
poisk_2(arc, x)
b = timeit.default_timer() - b
print(f"время - {b}\n")
print("поиск через отсортированный массив")
b = timeit.default_timer()
poisk_2(sorted(arc), x)
b = timeit.default_timer() - b
print(f"время - {b}\n")
print("поиск через дерево")
a = timeit.default_timer()
poisk(tree.root, x)
a = timeit.default_timer() - a
print(f"время - {a}")
