from btree import BinaryTree
from node import Node

tree = BinaryTree(Node('Paco', 6))

nodes = [
    ('Jose', 5),
    ('Rolf', 3),
    ('Anne', 7),
    ('Charlie', 11),
    ('Jen', 2)
]

for n in nodes:
    tree.add(Node(*n))

tree.flatten()
