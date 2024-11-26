# 고급 그래프 탐색

import heapq
import queue

graph = {
    'A': {'B':8, 'C':1,'D':2},
    'B': {},
    'C': {'B':5,'D':2},
    'D': {'E':3,'F':5},
    'E': {'F':1},
    'F': {'A':5}
    
}

def dijkstra(graph, start):
    distance = {node:float("inf") for node in graph}
    distance[start] = 0
    queue = []
    heapq.heappush(queue,[distance[start] , start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distance[current_node] < current_distance:
            continue
        
        for adjcent, weight in graph[current_node].items():
            cdistance = current_distance+weight
            if cdistance < distance[adjcent]:
                distance[adjcent] = cdistance
                heapq.heappush(queue, [cdistance, adjcent])
    return distance


print(dijkstra(graph, 'A'))

                