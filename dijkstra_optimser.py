import sys
import math
import heapq

def read_input():
    input_lines = sys.stdin.read().strip().splitlines()
    maps = [[float(x) for x in line.split(",")] for line in input_lines]
    return maps  

def shortest_path(map):
    n = map.pop(0)
    rocks = [(map[i], map[i + 1]) for i in range(0, len(map), 2)]
    graph = build_graph(rocks)
    return graph, len(rocks) - 1
    
def build_graph(rocks):
    graph = {i: [] for i in range(len(rocks))}
    for i in range(len(rocks)):
        for j in range(i + 1, len(rocks)):
            dist = math.sqrt((rocks[i][0] - rocks[j][0])**2 + (rocks[i][1] - rocks[j][1])**2)
            if dist <= 100:
                graph[i].append((j, dist))
                graph[j].append((i, dist))
    return graph

def dijkstra(graph, start, target):
    n = len(graph)
    dist = [float("inf")] * n
    color = ['white'] * n
    color[start] = 'grey'
    dist[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        
        if color[u] == 'black':
            continue
        
        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if color[v] == 'white':
                color[v] = 'grey'
                dist[v] = new_dist
                heapq.heappush(priority_queue, (new_dist, v))
            elif color[v] == 'grey' and new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(priority_queue, (new_dist, v))
        
        color[u] = 'black'
        if u == target:
            return dist[u]
    
    return -1

def main():    
    maps = read_input()
    results = []
    for map in maps:
        graph, target = shortest_path(map)
        cost = dijkstra(graph, 0, target)
        if cost == -1:
            results.append("-1")
        else:
            results.append("{:.2f}".format(cost)) 
    
    for result in results:
        print(result)

main()
