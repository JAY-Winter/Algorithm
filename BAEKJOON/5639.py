import sys
sys.setrecursionlimit(10**9)

# 입력 받기
lst = [int(line) for line in sys.stdin]
print(lst)
def solve(start, end):
    if start > end:
        return

    div = end + 1 # 오른쪽 서브트리 시작 지점 초기화
    # 현재 노드보다 큰 값(오른쪽 서브트리 시작 지점) 찾기
    for i in range(start + 1, end + 1):
        if lst[start] < lst[i]:
            div = i
            break

    # 왼쪽 서브트리 탐색
    solve(start + 1, div - 1)
    # 오른쪽 서브트리 탐색
    solve(div, end)
    # 후위 순회 결과 출력
    print(lst[start])

solve(0, len(lst) - 1)
