F, S, G, U, D = map(int, input().split())

INF = 1e9


def bfs():
    global INF
    dist = [INF] * (F + 1)
    dist[S] = 0
    Q = [S]
    while Q:
        cur = Q.pop(0)
        for d in (U, -D):
            head = cur + d
            if F + 1 > head >= 1 and dist[head] > dist[cur] + 1:
                dist[head] = dist[cur] + 1
                Q.append(head)
    return dist[G]


answer = bfs()
print(answer if answer != INF else 'use the stairs')