N, K = map(int, input().split())
answer = 1e9


def search(X, K):
    dist = [1e9 for _ in range(100001)]
    dist[X] = 0
    Q = [(X, 0)]
    while Q:
        x, s = Q.pop(0)
        for d in range(3):
            if d == 0:
                nx = x + 1
                ns = s + 1
            elif d == 1:
                nx = x - 1
                ns = s + 1
            elif d == 2:
                nx = 2 * x
                ns = s
            if 0 <= nx < 100001 and dist[nx] > ns:
                Q.append((nx, ns))
                dist[nx] = ns
    return dist[K]


answer = search(N, K)
print(answer)
