# Graph traversal potpourri
A collection of Python scripts used to solve graph traversal problems, written for COMPSCI220.

### duplicate_node_0.py

This script reads each digraph from the input and duplicates the node with index 0, giving it a new index of n, where n is the order of the original digraph. This new node has the same in and out neighbours as node 0 in the original digraph. At the end of each graph, the number of arcs that have been added by duplicating node 0 is printed.

Example output format:
```
5
1 3
2 3
0 4

1 3
3
4
1 2

1
1 2
2
0
```
The first line indicates the order of the new digraph (5), the next 5 lines are the 5 adjacency list showing the arcs of the digraph, and the 3 on line 7 indicates that three new arcs were added to the input digraph. The next line is a 4, which indicates that the next digraph has order 4, and so on. 

### tree_cross_arcs.py
This script performs DFS on each digraph starting from node 0 and prints out the total numbers of tree arcs and cross arcs that result from the traversal. **DFS is performed where the one with the lowest index is chosen when there is a choice between white or grey nodes.**

For each input digraph, a line is printed with the number of tree arcs, a white space, and then the number of cross arcs. 

Example output format:
```
3 0
2 1
```

For the first digraph, 3 would be the number of tree arcs, and 0 would be the number of cross arcs. There would be 2 tree arcs and 1 cross arc for the second. 

### closer_node_finder.py

For a given digraph of order n, this script can find whether node 0 or node 1 is closer to node n-1. The index of the closer node along with its distance to n-1. If both nodes are at the same distance, 0 is given as the output and the distance from 0 to n-1. When either of the nodes is unreachable from node n-1, the distance is infinity, which is outputted by the order of the digraph, n.

For each input digraph, an integer is printed with the index of the closer of the nodes, 0 or 1 to n-1 (or 0 is printed if both nodes have the same distance), then a white space and the distance of the printed node to n - 1, or n if the distance is infinite.

Example output format:
```
0 1
0 1
```

### directed_girth_finder.py

This script can find the directed girth of the graph, which is the length of the shortest cycle. If the digraph does not contain a cycle, the girth is undefined, meaning it has a girth of 0. The output will be just one integer per line sent to the console, each line representing the directed girth of every digraph fed in. 

Example output format:
```
3
0
```

### dijkstra_optimsation

A frog needs to navigate its way from its current position to its next meal through a landscape, and to do so, it leaps from rock to rock but can jump at most 1m each time. This script finds the shortest path length to get the frog to its next meal using only rocks. The landscape is a n x n square (units in cm) with the exact locations of rocks given by coordinates (x,y) where 0 is less or equal to x, y, which is less or equal to n. The rocks are scattered across the landscape, and the distance between rocks is calculated using Euclidean distance. This script takes the distance and uses the Dijkstra algorithm to solve the SSSP problem. 

For each input line, a single number is outputted to the console, displaying the shortest path length from the starting position to the next meal. If the next meal is unreachable from the origin, -1 is given as the output. 

Example output format:
```
200.00
-1
115.14
```

## Usage
All scripts except for "dijkstra_optimser" take in a specific digraph input format outlined below. "dijkstra_optimser" takes in a different format, which has its own section. All scripts read from standard input and write to standard output: 

`python script.py < input.txt > output.txt`

**Digraph input format:**

A sequence of one or more digraphs from the standard input (e.g. sys.stdin). Each graph is represented in the form of an adjacency list, where the first line is an integer n indicating the order of the graph, followed by n whitespace-separated lists of adjacencies for nodes labelled from 0 to n-1, where each graph is sorted. Each graph is terminated by a line consisting of one zero. Below is an example of two digraphs, where the first has a node set of {0, 1, 2, 3} and arc set {(0, 1), (0, 3), (1, 2), (1, 3), (2, 0)}, the
second has node set {0, 1, 2} and arc set {(0, 1), (0, 2), (2, 1)}.

```
4
1 3
2 3
0

3
1 2

1
0
```

**Dijkstra_optimser input format:**

Like the digraph input format, it is taken from the standard input as multiple lines of comma-separated numbers. Each line has 2p+1 numbers where p is greater or equal to 2. The first number on each line is the size of the landscape, n. 

The following 2p numbers give the locations of p rocks, so the jth rocks are at (2j, 2j+1).

The first position that is listed on each line is the current position of the frog, and the final position listed is the target rock where the frog will find the next meal. 

For example:
```
100,0,0,0,100,100,100
1000,20.892,986,602,138.97,206.2,10.44
200,25,25,10,1,50,25,140,30
```

## Credits
Huge shoutout to myself for writing this!!!
