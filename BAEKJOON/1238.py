import sys, heapq

def dijkstra(graph, start):
    distances = [float('inf')] * (N+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append([end, time])
    reverse_graph[end].append([start, time])

to_party = dijkstra(graph, X)
from_party = dijkstra(reverse_graph, X)

max_distance = max([to_party[i] + from_party[i] for i in range(1, N+1)])

print(max_distance)
