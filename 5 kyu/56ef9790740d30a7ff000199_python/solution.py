from collections import deque

class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

        
def tree_to_list(tree_root):
    queue = deque([tree_root])
    data_list = []
    while queue:
        node = queue.popleft()
        data_list.append(node.data)
        if node.child_nodes:
            queue.extend(node.child_nodes)
            
    return data_list