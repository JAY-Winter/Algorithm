N = int(input())
towers = list(map(int, input().split()))

stack = []
result = []

for idx, height in enumerate(towers):
    # 스택이 비어있지 않고, 스택의 맨 위 탑의 높이가 현재 탑의 높이보다 낮으면 pop
    while stack and stack[-1][1] < height:
        stack.pop()

    # 스택이 비어있으면 0을 결과에 추가 (신호를 수신하는 탑이 없음)
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0] + 1)  # 인덱스는 0부터 시작하므로 +1

    stack.append((idx, height))

print(' '.join(map(str, result)))
