'''
- 게임횟수 : X
- 이긴게임 : Y (Z%)
- Z : 형택이의 승률, 소수점은 버린다
- 예) X = 53, Y= 47 -> Z = 88

Q) X, Y 가 주어질 때, 형택이가 게임을 최소 몇 번 더해야 Z 가 변하는지 구하라
'''


def calculate(cnt):
    return ((Y + cnt) * 100) // (X + cnt)


# X < = 1억 -> 완탐 불가능 -> 이분탐색

X, Y = map(int, input().split())
init_Z = (Y * 100) // X

start, end = 1, 10 ** 9
answer = -1

while start <= end:
    mid = (start + end) // 2
    new_Z = (100 * (Y + mid)) // (X + mid)

    if new_Z > init_Z:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)
