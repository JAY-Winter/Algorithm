'''
격자판의 N번 행의 바로 아래(N+1) 의 모든 칸에는 성이 있다

- 궁수 3명을 배치할 것이다
    성이 있는 칸에 배치 가능
    하나의 칸에 최대 1명

- 각각의 턴마다 궁수는 적 하나 공격 가능
    모든 궁수는 동시에 공격한다

- 공격 가능 대상
    거리가 D 이하인 적 중에서 가장 가까운 적
    가장 왼쪽에 있는 적
    같은 적이 여러 궁수에게 공격 당할 수 있음
    공격 받으면 게임에서 제외

- 격자판의 두 위치 거리 계산
    distance = abs(r1-r2) + abs(c1-c2)

- 적의 이동
    궁수의 공격이 끝나면 적은 한 칸 아래로 이동한다
    성이 있는 칸으로 이동 시, 게임에서 제외

- 게임 종료
    모든 적이 게임에서 제외되면 게임 종료

- 0 : 빈 칸, 1 : 적

Q. 궁수의 공격으로 제거할 수 있는 적의 최대 수를 구하라

Sol)
3 <= N, M <= 15
총 225 칸
225 칸 중 3 개를 고르는 경우의 수
'''


def select_artchers(start, selected):
    global answer

    if len(selected) == 3:
        # 궁수는 항상 N+1 번째 행에 위치
        archer_position = [(N, col) for col in selected]
        round_answer = play(archer_position)
        answer = max(answer, round_answer)
        return

    for col in range(start, M):
        select_artchers(col + 1, selected + [col])



def find_enemy():
    enemy_position = []
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1:
                enemy_position.append((r, c))
    return enemy_position


def calculate_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def select_who_will_deleted_by_attack(archer_position, enemy_position):
    # 회차별 사라질 적
    enemy_who_will_deleted = []
    # 궁수별 공격할 수 있는 적을 고른다
    for archer in archer_position:
        archer_can_attack = []
        for enemy in enemy_position:
            distance = calculate_distance(*archer, *enemy)
            if distance <= D:
                archer_can_attack.append((distance, *enemy))
        # 궁수별 공격할 수 있는 적이 있으면
        if archer_can_attack:
            # 공격 기준 정렬
            temp_can_attack = sorted(archer_can_attack, key=lambda x: (x[0], x[2]))
            # 한 명을 고른다. 이때, 적의 좌표값만 넣어준다
            archer_attack_enemy = (temp_can_attack[0][1], temp_can_attack[0][2])
            enemy_who_will_deleted.append(archer_attack_enemy)
    return enemy_who_will_deleted


def move_enemy(enemy_position):
    temp_enemy_position = []
    for idx, enemy in enumerate(enemy_position):
        r, c = enemy
        nr, nc = r + 1, c
        # 성에 도달하면 삭제
        if nr >= N:
            enemy_position.pop(idx)
        else:
            temp_enemy_position.append((nr, nc))
    return temp_enemy_position


def play(archer_position):
    # 적의 위치 확인
    enemy_position = find_enemy()

    # 회차별 제거할 수 있는 적의 수
    round_deleted_cnt = 0

    # 게임 실행 -> 적이 존재하지 않을 때 까지
    while enemy_position:
        # 회차별 사라질 적
        enemy_who_will_deleted = select_who_will_deleted_by_attack(archer_position, enemy_position)

        # enemy_position 에서 위치한 적을 지운다
        for deleted_enemy in enemy_who_will_deleted:
            dr, dc = deleted_enemy
            for idx, enemy in enumerate(enemy_position):
                r, c = enemy
                if dr == r and dc == c:
                    enemy_position.pop(idx)
                    round_deleted_cnt += 1

        # 궁수의 공격이 끝나면, 적은 아래로 한 칸 이동한다
        temp_enemy_position = move_enemy(enemy_position)

        # 적의 위치 갱신
        enemy_position = temp_enemy_position

    return round_deleted_cnt


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

checked = [[False] * M for _ in range(N)]
archer_position = []
select_artchers(0, [])
print(answer)
