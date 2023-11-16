'''
Q) X 일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 확인하자
 - X 일 동안 가장 많이 들어온 방문자 수를 출력한다
    만약 최대 방문자 수가 0명이라면 SAD 를 출력한다
- 만약 최대 방문자 수가 0 명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 확인한다

'''

# N : 블로그를 시작하고 지난 일수
N, X = map(int, input().split())

# 1일차부터 N일차까지 하루 방문자 수
visited = list(map(int, input().split()))

max_visit = sum(visited[:X])  # 첫 X일 동안의 방문자 수
current_visit = max_visit
count = 1

for i in range(X, N):
    # 새로운 날의 방문자 수를 추가하고, 가장 오래된 날의 방문자 수를 뺌
    current_visit = current_visit + visited[i] - visited[i - X]

    # 최대 방문자 수 갱신
    if current_visit > max_visit:
        max_visit = current_visit
        count = 1  # 새로운 최대값이므로 카운트 초기화
    elif current_visit == max_visit:
        count += 1  # 동일한 최대값 발견 시 카운트 증가

if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(count)
