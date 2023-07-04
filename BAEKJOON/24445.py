N, M, R = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(N):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

# i 번째 줄에는 정점 i의 방문순서를 출력한다
# 시작 정점의 방문순서는 1이다
# 인접 정점은 내림차순으로 방문한다


cnt = 1
visited = [0] * (N+1)
visited[R] = cnt

Q = [R]
while Q:
    node = Q.pop(0) 
    for new_node in sorted(adj_list[node], reverse=True):
        if not visited[new_node]:
            cnt += 1
            visited[new_node] = cnt
            Q.append(new_node)

print(*visited[1:], sep='\n')