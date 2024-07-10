import sys

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
            cur_digraph.append({j:list(map(int, input_lines[i].split()))})
            i += 1
    
    cur_dict = {}
    for d in cur_digraph:
        for key, value in d.items():
            cur_dict[key] = value
    
    digraphs.append(cur_dict)


def dfs(digraph):
    node_count = len(digraph)
    color = ["white"] * node_count
    seen = [0] * node_count
    done = [0] * node_count
    time = [0]
    pred = [-1] * node_count

    for node in digraph:
        if color[node] == "white":
            dfsvisit(node, digraph, color, seen, done, time, pred)

    return seen, done, pred

def dfsvisit(node, digraph, color, seen, done, time, pred):
    stack = [node]
    color[node] = 'grey'
    seen[node] = time[0]
    time[0] += 1
    
    while stack:
        u = stack[-1]
        all_neighbors_visited = True
        if u in digraph:
            for v in sorted(digraph[u]):
                if color[v] == 'white':
                    color[v] = 'grey'
                    seen[v] = time[0]
                    pred[v] = u
                    time[0] += 1
                    stack.append(v)
                    all_neighbors_visited = False
                    break
        if all_neighbors_visited:
            stack.pop()
            color[u] = "black"
            done[u] = time[0]
            time[0] += 1

def arc_counter(seen, done, pred):
    tree_arcs = 0
    cross_arcs = 0
    for v in range(len(pred)):
        if pred[v] != -1:
            tree_arcs += 1
    
    for u in range(len(seen)):
        if u in digraph:
            for v in digraph[u]:
                if seen[v] < done[v] < seen[u] < done[u]:
                    cross_arcs += 1
                
    return tree_arcs, cross_arcs

for digraph in digraphs:
    seen, done, pred = dfs(digraph)
    print(seen, done, pred)
    tree, cross = arc_counter(seen, done, pred)
    print(str(tree) + " " + str(cross))


