N, M = map(int, input().split())
# M 개의 줄에 간선의 양 끝점 u, v 가 주어진다
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
    
visited = [0] * (N+1)
visited[0] = 1

cnt = 0
for idx, node in enumerate(adj_list):
    if not visited[idx]:
        visited[idx] = 1
    
        Q = [node]
        while Q:
            nodes = Q.pop(0)

            for nod in nodes:
                if not visited[nod]:
                    visited[nod] = 1
                    Q.append(adj_list[nod])
        cnt += 1

print(cnt)
        