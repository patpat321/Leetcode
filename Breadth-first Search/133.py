"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        queue = [node]
        copy = UndirectedGraphNode(node.label)
        check = {node:copy}
        while queue:
            nd = queue.pop()
            for neighbor in nd.neighbors:
                if neighbor not in check:
                    copy = UndirectedGraphNode(neighbor.label)
                    check[neighbor] = copy
                    check[nd].neighbors.append(copy)
                    queue.insert(0, neighbor)
                else:
                    check[nd].neighbors.append(check[neighbor])
        return check[node]
"""
Use dictionary to build a hashtable for all new node to old node, and to keep track of the node that is visited.
"""
