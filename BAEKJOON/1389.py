N, M = map(int, input().split())
friends = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    friends[A].append(B)
    friends[B].append(A)


def search(node, dist):

    for search_node in range(1, N+1):
        if search_node == node:
            continue
        else:
            Q = [node]
            
            while Q:
                node = Q.pop(0)
                for adj_node in friends[node]:
                    if dist[adj_node] == -1:
                        dist[adj_node] = dist[node] + 1
                        Q.append((adj_node))



answer = {num : 0 for num in range(1, N+1)}
# 각 숫자를 순회하면서 해당 숫자 외 모든 숫자에 대해 도달하는 시간이 얼마나 걸리는지 확인
for node in range(1, N+1):
    temp_cnt = 0
    dist = [-1 for _ in range(N+1)]
    dist[node] = 0
    search(node, dist)
    node_sum = sum(dist[1:])
    answer[node] = node_sum
    


answer = sorted(answer.items(), key=lambda x: (x[1]))
print(answer[0][0])
