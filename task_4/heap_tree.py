import matplotlib.pyplot as plt
import networkx as nx
import uuid

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color 
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
   
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)} 

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title('Binary Heap Visualization')
    plt.show()

def build_heap_tree(heap_values):

    def create_heap_tree(index):
    
        if index >= len(heap_values):
            return None
        node = Node(heap_values[index])
        node.left = create_heap_tree(2 * index + 1)  
        node.right = create_heap_tree(2 * index + 2)  
        return node

    root = create_heap_tree(0)
    draw_heap(root)

# TO TEST
heap_values = [10, 20, 30, 40, 50, 60]  
build_heap_tree(heap_values)
