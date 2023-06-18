from collections import deque
# K : 테스트 케이스 수
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    colors = [0] * (V+1)

    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)


    def bfs(node):
        color = 1
        Q = [(node, color)]
        Q = deque([(node, color)])
        colors[node] = color
        while Q:
            node, color = Q.popleft()
            for adj_node in adj[node]:
                if not colors[adj_node]:
                    colors[adj_node] = -color
                    Q.append((adj_node, -color))
        
    for i in range(1, V+1):
        if not colors[i]:
            bfs(i)

    flag = True
    for i in range(1, V+1):
        for j in adj[i]:
            if colors[i] == colors[j]:
                flag = False
    print('YES' if flag else 'NO')