N = int(input())
A = list(map(int, input().split()))

temp_answer = []
selected = [0 for _ in range(N)]
def recur(n, temp):
    if n == N:
        # temp_answer.append(temp)
        flag = True
        for i in range(0, len(temp)-1, 2):
            if A[temp[i]] < A[temp[i-1]]:
                flag = False
        if flag:
            temp_answer.append(temp)
        return
    
    for i in range(N):
        if not selected[i]:

            # if (temp[i] >= temp[n]):
            selected[i] = 1
            recur(n+1, temp + [i])
            selected[i] = 0

recur(0, [])

print(temp_answer)
# for temp in temp_answer:
#     for answer in zip(A, temp):
#         print(answer[0], end=' ')
#     print()