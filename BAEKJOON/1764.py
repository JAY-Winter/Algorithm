# # N : 듣도 못한 사람의 수 <= 50만
# # M : 보도 못한 사람의 수 <= 50만
# N, M = map(int, input().split())
# 듣도_못한_사람 = [input() for _ in range(N)]
# 보도_못한_사람 = [input() for _ in range(M)]

# # print(듣도_못한_사람)
# # print(보도_못한_사람)

# # 듣도 보도 못한 사람의 명단을 구하라
# all_person = 듣도_못한_사람 + 보도_못한_사람
# # print(all_person)

# person_dict = {}
# for person in all_person:
#     if person_dict.get(person):
#         person_dict[person] += 1
#     else:
#         person_dict[person] = 1

# # print(person_dict)

# sorted_person_dict = sorted(person_dict.items(), key=lambda x: (-x[1], x[0]))
# # print(sorted_person_dict)

# answer_list = []
# for person, cnt in sorted_person_dict:
#     if cnt >= 2:
#         answer_list.append(person)
#     else:
#         break

# print(len(answer_list))
# print(*answer_list, sep='\n')


import sys
si = sys.stdin.readline
n, m = list(map(int, si().split()))
a = sorted([si() for _ in range(n)])
b = sorted([si() for _ in range(m)])

def bin_search(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            l = mid + 1
        else: 
            r = mid - 1
    return False

ans = [x for x in b if bin_search(a, 0, n-1, x)]
print(len(ans))
for x in ans:
    print(x, end="")