'''
- 총 F층
- 현재 S 층이고 G 층으로 이동하고자 함
- 위, 아래 버튼만 존재함
Q) G층에 도착하기 위해 최소 몇 번의 버튼을 눌러야하는가?
    만약, 도착할 수 있으면 "use the stairs" 를 출력하라
'''


def bfs():
    start_stair = S
    distance = [987654321] * (F + 1)
    distance[start_stair] = 0

    Q = [start_stair]
    while Q:
        current_stair = Q.pop(0)

        if current_stair == G:
            return distance[current_stair]

        for new_stair in (current_stair + U, current_stair - D):
            if new_stair > F or new_stair < 1:
                continue

            if distance[current_stair] + 1 >= distance[new_stair]:
                continue

            distance[new_stair] = distance[current_stair] + 1
            Q.append(new_stair)

    return "use the stairs"


F, S, G, U, D = map(int, input().split())
print(bfs())
