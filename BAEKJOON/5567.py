n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


selected = [0 for _ in range(n+1)]
selected[1] = 1
answer = 0
def bfs(node):
    global answer
    cnt = 0
    Q = [(node, cnt)]
    while Q:
        node, cnt = Q.pop(0)
        if cnt == 2:
            break
        
        for adj_node in adj[node]:
            if not selected[adj_node]:
                selected[adj_node] = 1
                Q.append((adj_node, cnt+1))
                answer += 1

bfs(1)
print(answer)