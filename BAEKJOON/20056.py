'''
- board : N*N
- 파이어볼 M 개를 발사한다
    가장 처음에 파이어볼은 각자 위치에서 이동을 대기한다
- i번 파이어볼
    위치 : (ri, ci)
    질량 : mi
    방향 : di
    속력 : si

- board 행,열은 1번부터 N번까지
    -> -1 씩 해줘야함

- 파이어볼의 방향 : 인접한 8개의 칸 상 -> 우 -> 하 -> 좌 순

- 이동 명령 시 발생하는 일
    1. 모든 파이어볼이 자신의 방향 di 로 속력 si칸 만큼 이동한다
        이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다
    2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서 다음과 같은 일이 일어난다
        1. 같은 칸에 있는 파이어볼은 하나로 합쳐진다
        2. 파이어볼은 4개의 파이어볼로 나누어진다
        3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다
            1) 질량 : 합쳐진 파이어볼 질량의 합 / 5
            2) 속력 : 합쳐진 파이어볼 속력의 합 / 합쳐진 파이어볼 개수
            3) 방향 : 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
        4. 질량이 0인 파이어볼은 사라진다


Q. 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자
'''

N, M, K = map(int, input().split())

fireball_info = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball_info.append((r-1, c-1, m, s, d))

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


# r, c좌표 값을 key 값으로 변환
def convert_position_to_key(r, c, N):
    return (N * r) + c


def convert_key_to_position(key, N):
    return key // N, key % N


# 이동을 K번 명령한다
for k in range(K):
    moved_fireball_info = {}
    for fireball in fireball_info:
        r, c, m, s, d = fireball

        # 모든 파이어볼이 자신의 방향 d로 속력s칸 만큼 이동한다
        nr = (r + s * dr[d]) % N
        nc = (c + s * dc[d]) % N

        # 새로 도착한 좌표를 key 값으로 변환
        position_key = convert_position_to_key(nr, nc, N)

        # 방향 d로 속력 s만큼 이동한 새로운 r, c 좌표에 대해 좌표값을 position_key 값으로 변환후 value 할당
        if position_key not in moved_fireball_info:
            moved_fireball_info[position_key] = [(m, s, d)]
        else:
            moved_fireball_info[position_key] += [(m, s, d)]

    temp_fireball_info = []
    # 이동이 모두 끝난 뒤 일어나는 일
    for position_key, balls in moved_fireball_info.items():
        # 다시 position_key 값을 좌표값으로 변환
        r, c = convert_key_to_position(position_key, N)

        # 2개 이상의 파이어볼이 위치한 곳
        if len(balls) >= 2:
            # 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다
            new_m = sum(fireball[0] for fireball in balls) // 5
            new_s = sum(fireball[1] for fireball in balls) // len(balls)
            # 질량이 0인 파이어볼은 소멸되어 없어진다
            if new_m == 0:
                continue

            # 합쳐지는 파이어볼의 방향 확인 : 모두 홀수 혹은 짝수인지에 대한 여부 판단
            first_d = balls[0][2] % 2
            flag = True
            for fireball in balls[1:]:
                next_d = fireball[2] % 2
                if next_d != first_d:
                    flag = False
                    break

            # 새로 할당될 파이어볼 정보
            new_fire_ball_info = []
            if flag:
                # 모두 홀수이거나 짝수면 방향은 0, 2, 4, 6 이 된다
                for new_d in range(0, 8, 2):
                    new_fire_ball_info.append((r, c, new_m, new_s, new_d))
            else:
                # 그렇지 않으면 방향은 1, 3, 5, 7 이 된다
                for new_d in range(1, 8, 2):
                    new_fire_ball_info.append((r, c, new_m, new_s, new_d))
            temp_fireball_info += new_fire_ball_info
        # 2개 미만의 파이어볼이 위치한 좌표
        else:
            # 질량이 0이 아닐 때 업데이트
            if balls[0][0] != 0:
                temp_fireball_info.append((r, c) + balls[0])
    # 새로운 값으로 대체
    fireball_info = temp_fireball_info
    if k == K - 1:
        answer = sum(ball[2] for ball in fireball_info)
# K번 명령한 후, 남아있는 파이어볼 질량의 합

print(answer)
