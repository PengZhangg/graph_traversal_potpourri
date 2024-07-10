from collections import deque
import sys

def read_input():
    input_lines = sys.stdin.read().strip().splitlines()
    digraphs = []
    i = 0

    while i < len(input_lines):
        node_count = int(input_lines[i])
        i += 1
        
        if node_count == 0:
            break
        
        cur_digraph = {}
        for j in range(node_count):
            if i < len(input_lines):
                cur_digraph[j] = list(map(int, input_lines[i].split()))
                i += 1
        
        digraphs.append(cur_digraph)
    
    return digraphs

def bfs(digraph, root):
    queue = deque([root])
    node_count = len(digraph)
    color = ["white"] * node_count
    pred = [-1] * node_count
    d = [node_count] * node_count
    
    color[root] = 'grey'
    d[root] = 0

    while queue:
        u = queue.popleft()
        for v in digraph.get(u, []):
            if color[v] == 'white':
                color[v] = 'grey'
                pred[v] = u
                d[v] = d[u] + 1
                queue.append(v)
            elif v == root:
                return d[u] + 1 
        color[u] = 'black'
    
    return float("inf")

def main():
    digraphs = read_input()
    results = []
    for digraph in digraphs:
        min_girth = float("inf")
        for node in digraph:
            girth = bfs(digraph, node)
            if girth < min_girth:
                min_girth = girth
        results.append(min_girth if min_girth != float("inf") else 0)
    
    for result in results:
        print(result)

main()
