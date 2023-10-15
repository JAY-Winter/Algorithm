V = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    cur_line = list(map(int, input().split()))[:-1]
    for i in range(1, len(cur_line) - 1, 2):
        node1, node2, weight = cur_line[0], cur_line[i], cur_line[i + 1]
        graph[node1].append((node2, weight))

answer_cost = -987654321


def dfs(cur_node, visited):
    visited[cur_node] = True
    max_distance = 0
    farthest_node = cur_node
    for adj_node, weight in graph[cur_node]:
        if not visited[adj_node]:
            next_node, next_distance = dfs(adj_node, visited)
            if next_distance + weight > max_distance:
                max_distance = next_distance + weight
                farthest_node = next_node
    return farthest_node, max_distance


# 임의의 노드에서 시작
start_node, _ = dfs(1, [False] * (V + 1))

# 가장 먼 노드에서 다시 시작
_, answer_cost = dfs(start_node, [False] * (V + 1))

print(answer_cost)
