from collections import deque
import sys

def read_input():
    input_lines = sys.stdin.read().strip().splitlines() 
    digraphs = []
    i = 0
    
    while i < len(input_lines):
        cur_digraph = []
        node_count = int(input_lines[i])  
        i += 1
        
        if node_count == 0:
            break
        
        for j in range(node_count):
            if i < len(input_lines):
                cur_digraph.append((j, list(map(int, input_lines[i].split()))))
                i += 1
        
        cur_dict = {}
        for node, edges in cur_digraph:
            cur_dict[node] = edges
        
        digraphs.append(cur_dict)
        
    return digraphs

def bfs(digraph, root):
    queue = deque()
    node_count = len(digraph)
    color = ["white"] * node_count
    pred = [-1] * node_count
    d = [node_count] * node_count
    
    queue.append(root)
    color[root] = 'grey'
    d[root] = 0
    
    bfsvisit(digraph, queue, color, pred, d)

    return d
    
def bfsvisit(digraph, queue, color, pred, d):
    while queue:
        u = queue.popleft()
        if u in digraph:
            for v in sorted(digraph[u]):
                if color[v] == 'white':
                    color[v] = 'grey'
                    pred[v] = u
                    d[v] = d[u] + 1
                    queue.append(v)
            color[u] = 'black'

def distance_finder(d0, d1, n):
    dist0 = d0[n-1]
    dist1 = d1[n-1]
    
    if dist0 < dist1:
        print(f"0 {dist0}")
    elif dist0 > dist1:
        print(f"1 {dist1}")
    else:
        print(f"0 {dist0}")

def main():
    digraphs = read_input()
    for digraph in digraphs:
        n = len(digraph)
        d0 = bfs(digraph, 0)
        print(f"depth list of bfs starting at node 0: {d0}")
        d1 = bfs(digraph, 1)
        print(f"depth list of bfs starting at node 1: {d1}")
        distance_finder(d0, d1, n)

digraphs = read_input()
for digraph in digraphs:
    for node in digraph:
        d = bfs(digraph, node)
        print(d)