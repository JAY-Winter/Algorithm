# A, B <= 10**9
A, B = map(int, input().split())

# Q : A -> B 로 바꾸는데 필요한 연산의 최솟값
answer = -1
def search(n, num):
    global answer
    # 연산 경우
    # 1. 2를 곱한다
    # 2. 1을 수의 가장 오른쪽에 추가한다

    if num > B:
        return
    if num == B:
        answer = n
    
    search(n+1, num * 2)
    search(n+1, num * 10 + 1)

search(1, A)

print(answer)