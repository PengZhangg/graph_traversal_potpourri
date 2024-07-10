import sys

input_lines = sys.stdin.read().strip().splitlines()
    
digraphs = []
i = 0

while i < len(input_lines):
    cur_digraph = []
    
    node_count = int(input_lines[i])
    if node_count == 0:
        break
    
    cur_digraph.append(node_count)
    i += 1
    
    for j in range(node_count):
        if i < len(input_lines):
            cur_digraph.append(input_lines[i].strip())
            i += 1
    
    digraphs.append(cur_digraph)

new_digraphs = []

for digraph in digraphs:
    node_count = len(digraph)
    new_node = str(digraph[0])
    new_digraph = [int(new_node) + 1]
    arcs = 0
    digraph.pop(0)
    
    arcs += sum(1 for char in digraph[0].strip() if not char.isspace())

    for node in digraph:
        if node == "0":
            node += " " + new_node
            arcs += 1
        
        new_digraph.append(node)
        
    new_digraph.append(digraph[0])
    new_digraph.append(arcs)
    new_digraphs.append(new_digraph)

for graph in new_digraphs:
    for node in graph:
        print(str(node))
print("0")