import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.data) 
        if node.left:
            graph.add_edge(node.data, node.left.data)
            l = x - 1 / 2 ** layer
            pos[node.left.data] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.data, node.right.data)
            r = x + 1 / 2 ** layer
            pos[node.right.data] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited):
    tree = nx.DiGraph()
    pos = {tree_root.data: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = []
    for node in tree.nodes():
        if node in visited:
           
            color_value = int((visited.index(node) / len(visited)) * 255)
            colors.append(f'#{color_value:02x}FF{(255 - color_value):02x}')  
        else:
            colors.append('#FFFFFF')  

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, node_size=2500, node_color=colors, with_labels=True, arrows=False)
    plt.show()

def dfs(tree_root):
    visited = []
    stack = [tree_root]

    while stack:
        node = stack.pop()
        if node.data not in visited:
            visited.append(node.data)
           
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return visited

def bfs(tree_root):
    visited = []
    queue = deque([tree_root])

    while queue:
        node = queue.popleft()
        if node.data not in visited:
            visited.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return visited

# TO TEST
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

# DFS
visited_dfs = dfs(root)
draw_tree(root, visited_dfs)

#BFS
visited_bfs = bfs(root)
draw_tree(root, visited_bfs)
