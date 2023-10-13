'''
- 항상 다음 수는 앞 수 * a + b 이다

Q) 수 N개가 주어졌을 때, 규칙에 맞는 다음 수를 구하라

'''

#
# def find_a_b():
#     INF = 100
#
#     for i in range(-INF, INF):
#         for j in range(-INF, INF):
#             a, b = i, j
#             checked = [False] * len(numbers)
#             dfs(0, a, b, checked)
#             if all(checked[:-1]):
#                 return True, a, b
#     return False, 0, 0


def dfs(n, a, b, checked):
    if n == len(numbers) - 1:
        return

    if numbers[n + 1] == numbers[n] * a + b:
        checked[n] = True
        dfs(n + 1, a, b, checked)


N = int(input())
numbers = list(map(int, input().split()))

if N == 1:
    print('A')
elif N == 2:
    if numbers[0] == numbers[1]:
        print(numbers[1])
    else:
        print('A')
else:
    if numbers[1] - numbers[0] == 0:
        a = 1
        b = 0
    else:
        a = (numbers[2] - numbers[1]) // (numbers[1] - numbers[0])
        b = numbers[1] - numbers[0] * a

    checked = [False] * len(numbers)
    dfs(0, a, b, checked)
    if all(checked[:-1]):
        result = numbers[-1] * a + b
    else:
        result = 'B'

    print(result)