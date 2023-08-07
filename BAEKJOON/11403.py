N = int(input())
graph = [[] for _ in range(N+1)]
for r in range(N):
    line = list(map(int, input().split()))
    for idx, el in enumerate(line):
        if el:
            graph[r].append(idx)

visited = [[0] * N for _ in range(N)]


def dfs(parent_node, cur_node):
    for adj_node in graph[cur_node]:
        if not visited[parent_node][adj_node]:
            visited[parent_node][adj_node] = 1
            dfs(parent_node, adj_node)


for node in range(N):
    dfs(node, node)

for line in visited:
    print(*line)

