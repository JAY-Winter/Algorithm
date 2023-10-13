'''
-
Q) 1 에서 시작해 N 까지 도달해야한다. 이때, 최소한의 소들을 만나면서 가자
'''

import heapq


def dijk():
    INF = 1e9
    distances = [INF] * (N + 1)
    distances[1] = 0

    # (거리, 노드번호) 형태로 시작 노드 초기화
    Q = [(0, 1)]
    while Q:
        # 가장 짧은 거리의 노드를 꺼낸다
        print(Q)
        cur_distance, cur_node = heapq.heappop(Q)

        # 이미 처리된 노드라면 무시
        if distances[cur_node] < cur_distance:
            continue

        for adj_node, distance in graph[cur_node]:
            if distances[adj_node] > cur_distance + distance:
                distances[adj_node] = cur_distance + distance
                heapq.heappush(Q, (distances[adj_node], adj_node))

    return distances[N]


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

answer = dijk()
print(answer)
