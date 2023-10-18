'''
- n 개의 도시가 있다(2<=n<=100)
- 도시간 m 개의 버스가 있다(1<=m<=100,000)

Q) 모든 도시의 쌍(A, B)에 대해서 A->B 로 가는데 필요한 비용의 최솟값을 구하라
'''

n = int(input())
m = int(input())

grpah = [[] for _ in range(n + 1)]
INF = 1e9

cost_graph = [[int(INF)] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    cost_graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost_graph[a][b] = min(cost_graph[a][b], c)

# 플로이드 와샬 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost_graph[i][j] = min(cost_graph[i][j], cost_graph[i][k] + cost_graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cost_graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost_graph[i][j], end=' ')
    print()
