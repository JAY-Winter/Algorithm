N = int(input())
candidates = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0


def cal(candidate):
    global answer

    # 총 감독관
    candidate -= B
    answer += 1

    # 부감독관
    if candidate > 0:
        answer += candidate // C
        if candidate % C != 0:
            answer += 1


for candidate in candidates:
    cal(candidate)

print(answer)
