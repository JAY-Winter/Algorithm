import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
START, END = map(int, input().split())
INF = 1e9
dist = [INF] * (n + 1)
dist[START] = 0
routes = [[] for _ in range(n + 1)]


def dfs(e, next, route):
    if next == e:
        routes[next] = route

    for adj_node, time in graph[next]:
        if dist[adj_node] > dist[next] + time:
            dist[adj_node] = dist[next] + time
            dfs(e, adj_node, route + [adj_node])


path = [-1] * (n + 1)

def dijk():
    Q = [START]
    while Q:
        cur_node = Q.pop(0)
        for adj_node, time in graph[cur_node]:
            if dist[adj_node] > dist[cur_node] + time:
                dist[adj_node] = dist[cur_node] + time
                Q.append(adj_node)
                path[adj_node] = cur_node



dijk()

routes = []
temp = END
while temp != -1:
    routes.append(temp)
    temp = path[temp]


print(dist[END])
print(len(routes))
print(*routes[::-1])


