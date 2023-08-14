import sys
import heapq

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())


def dijk(start_node):
    INF = 1e9
    dist = [INF] * (N + 1)
    dist[start_node] = 0

    heap = []
    heapq.heappush(heap, [0, start_node])
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        if cur_dist > dist[cur_node]:
            continue

        for adj_node, time in graph[cur_node]:
            new_dist = dist[cur_node] + time
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                heapq.heappush(heap, [new_dist, adj_node])
    return dist


# 1 -> N
dist1 = dijk(1)
# v1 -> N
dist2 = dijk(v1)
# v2 -> N
dist3 = dijk(v2)

answer = min(dist1[v1] + dist2[v2] + dist3[N], dist1[v2] + dist3[v1] + dist2[N])
if answer >= 1e9:
    print(-1)
else:
    print(answer)
