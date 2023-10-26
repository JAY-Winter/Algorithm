'''
- 그래프
    지역별 양방향 통행 가능
    일정한 길이 1 ~ 15 탐색 가능

Q) 일정한 길이 이내의 모든 지역의 아이템을 습득 가능하다고 할 때, 얻을 수 있는 아이템의 최대 개수를 구하라
-
'''

# n : 지역의 개수, m : 수색 범위, r : 길의 개수
n, m, r = map(int, input().split())

# 구역별 아이템 수
item_by_city = list(map(int, input().split()))

adj_graph = [[] for _ in range(n)]
for _ in range(r):
    # a, b : 연결된 지역의 번호, l : 길의 길이
    a, b, l = map(int, input().split())
    # 연결된 구역은 양방향 통행이 가능하다
    adj_graph[a - 1].append((b - 1, l))
    adj_graph[b - 1].append((a - 1, l))


def dijk(city):
    result = 0
    INF = 1e9

    # 어떤 구역에서 아이템을 획득했는지
    visited = [False] * (n)
    visited[city] = True
    result += item_by_city[city]

    # 구역에 도착할 때 까지 소모된 길이 -> 최대값으로 초기화
    distance_to_city = [INF] * n
    # 시작점은 0
    distance_to_city[city] = 0
    Q = [(city)]
    while Q:
        cur_city = Q.pop(0)
        for adj_city, distance in adj_graph[cur_city]:
            # 현재 구역에서 인접한 다음 구역까지 소모되는 거리 길이가 최대 수색범위 m 을 벗어나는 경우는 피한다
            if distance_to_city[cur_city] + distance > m:
                continue

            # 현재 구역에서 인접한 다음 구역까지 소모되는 거리 길이가 해당 구역까지 도달할 수 있는 기존 거리 길이보다 짧은 경우 더 짧은 길이로 갱신해준다
            if distance_to_city[adj_city] > distance_to_city[cur_city] + distance:
                distance_to_city[adj_city] = distance_to_city[cur_city] + distance
                Q.append(adj_city)

                # 해당 구역에 처음 방문했을 경우에만 아이템을 획득한다
                if not visited[adj_city]:
                    result += item_by_city[adj_city]
                visited[adj_city] = True
    return result


answer = 0
# 지역별 탐색을 진행해야함
for i in range(n):
    temp_result = dijk(i)
    answer = max(answer, temp_result)

print(answer)
