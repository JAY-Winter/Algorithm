import sys
sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
cnt = 1


# i 번째 줄에는 정점 i 의 방문 순서를 출력한다
def dfs(cur_node):
    global cnt
    visited[cur_node] = cnt

    graph[cur_node].sort()
    for adj_node in graph[cur_node]:
        if not visited[adj_node]:
            cnt += 1
            dfs(adj_node)


#

dfs(R)

for i in range(1, N+1):
    print(visited[i])
