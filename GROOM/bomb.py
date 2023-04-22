# https://level.goorm.io/exam/159666/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%A8%BC%EB%8D%B0%EC%9D%B4-%ED%8F%AD%ED%83%84-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0/quiz/1
# r = y, c = x
# K 개의 폭탄
# 모든 폭탄의 초기값 0
# 폭탄이 떨어지면 상하좌우 인접칸이 1씩 증가


N, K = map(int, input().split())
arr = [[0] * N for _ in range(N)]

def bomb(y, x):
	arr[y][x] += 1
	dy = [-1, 1, 0, 0]	
	dx = [0, 0, -1, 1]
	
	for d in range(4):
		new_y = y + dy[d]
		new_x = x + dx[d]
		
		if new_y < N and new_y >= 0 and new_x < N and new_x >= 0:
			arr[new_y][new_x] += 1
		

for _ in range(K):
	y, x = map(int, input().split())
	y -= 1
	x -= 1
	bomb(y, x)

answer = 0

for i in range(N):
	answer += sum(arr[i])
	
print(answer)
	
	