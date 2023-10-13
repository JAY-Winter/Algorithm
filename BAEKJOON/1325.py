'''
N <= 10,000
M <= 100,000

Q) 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력
'''
from collections import deque


def bfs(node):
    hacking = 0

    visited = [False] * (N + 1)
    visited[node] = True

    Q = deque([node])
    while Q:
        cur_node = Q.popleft()
        for adj_node in graph[cur_node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                hacking += 1
                Q.append(adj_node)
    return hacking


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())

    graph[B].append(A)

answer = 0
answer_list = []
for i in range(1, N + 1):
    temp_answer = bfs(i)
    if temp_answer >= answer:
        if temp_answer > answer:
            answer = temp_answer
            answer_list = [i]
        else:
            answer_list.append(i)

print(*answer_list)
