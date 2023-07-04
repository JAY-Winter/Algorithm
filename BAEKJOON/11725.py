N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

parent = [-1 for _ in range(N+1)]
parent[1] = 0


def dfs(node):
    
    for adj_node in adj[node]:
        if parent[adj_node] == -1:
            parent[adj_node] = node
            dfs(adj_node)
dfs(1)

for node in parent[2:]:
    print(node)