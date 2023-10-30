# N = int(input())
#
# first = [i for i in range(1, N + 1)]
# second = [int(input()) for _ in range(N)]
#
#
# checked = [0] * N
#
# answer = 0
# answer_numbers = None
#
#
# def comb(checked):
#     global answer, answer_numbers
#
#     comb_numbers = []
#     for i in range(len(checked)):
#         if checked[i]:
#             comb_numbers.append(i)
#
#     first_comb = []
#     second_comb = []
#     for number in comb_numbers:
#         first_comb.append(first[number])
#         second_comb.append(second[number])
#
#     if set(first_comb) == set(second_comb):
#         if len(first_comb) > answer:
#             answer = len(first_comb)
#             answer_numbers = sorted(first_comb)
#         return
#
#
# def dfs(n, prev):
#     comb(checked)
#
#     if n == N:
#         return
#
#     for i in range(prev, N):
#         if not checked[i]:
#             checked[i] = 1
#             dfs(n + 1, i)
#             checked[i] = 0
#
#
# dfs(0, 0)
#
# print(answer)
# for number in answer_numbers:
#     print(number)


# Solution2

N = int(input())
second = [int(input()) for _ in range(N)]


def dfs(start, current):
    if visited[current]:
        if current == start:
            return True
        else:
            return False
    visited[current] = True
    return dfs(start, second[current] - 1)


result = []
for i in range(N):
    visited = [False] * N
    if dfs(i, i):
        result.append(i + 1)

print(len(result))
for num in result:
    print(num)
