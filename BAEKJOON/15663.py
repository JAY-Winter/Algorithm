N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
# print(arr)
# N 개 중에서 M 고르다

# 중복 X
# 사전 순으로 증가
nums_dict = {}
sel = [0 for _ in range(len(arr)+1)]
def search(n, temp):
    if n == M:
        temp_key = ''
        for t in temp:
            # print(arr[t], end=' ')
            temp_key += str(arr[t])
        # print('temp_key',temp_key)
        # print(temp)
        if not nums_dict.get(temp_key):
            nums_dict[temp_key] = 0
        # print()
        return
    
    for i in range(0, len(arr)):
        if not sel[i]:
            sel[i] = 1
            # print(temp)
            temp_2 = temp + [i]
            temp_key = ''
            for t in temp_2:
                temp_key += str(arr[t])
            if not nums_dict.get(temp_key):
            # print('temp2_key', temp_key)
                search(n+1, temp + [i])
                sel[i] = 0


search(0, [])

# print(nums_dict)

sorted_nums_dict = sorted(nums_dict)
for nums in sorted_nums_dict:
    for num in nums:
        print(num, end=' ')
    print()