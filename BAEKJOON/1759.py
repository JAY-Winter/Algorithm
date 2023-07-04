L, C = map(int, input().split())
strings = sorted(input().split())
# print(strings)
모음_기준 = ['a','e','i','o','u']
모음 = []
자음 = []
for s in strings:
    if s not in 모음_기준:
        자음.append(s)
    else:
        모음.append(s)

# 모음.sort()
# 자음.sort()
# print(모음, 자음)

sel_모음 = [0 for _ in range(len(모음))]
sel_자음 = [0 for _ in range(len(자음))]
string_dict = {}
def search(temp):
    if len(temp) == L:
        # print(temp)
        cnt_자음 = 0
        for t in temp:
            if t in 자음:
                cnt_자음 += 1
        if cnt_자음 >= 2:
            temp_str = ''.join(sorted(temp))
            
            if not string_dict.get(temp_str):
                string_dict[temp_str] = 1
                # print(temp_str)
            return
    # 모음 고르기
    for idx, mo in enumerate(모음):
        if not sel_모음[idx]:
            sel_모음[idx] = 1
            search(temp + [mo])
            sel_모음[idx] = 0
    # 자음 고르기
    if temp:
        for idx, ja in enumerate(자음):
            if not sel_자음[idx]:
                sel_자음[idx] = 1
                search(temp + [ja])
                sel_자음[idx] = 0
                
# search([])

sel = [0 for _ in range(len(strings))]
def search2(temp, start):
    print(start)
    if len(temp) == L:
        모음_개수 = 0
        자음_개수 = 0
        for t in temp:
            if t in 모음_기준:
                모음_개수 += 1
            else:
                자음_개수 += 1
        if 모음_개수 >= 1 and 자음_개수 >= 2:   
            temp = ''.join(temp)
            # print(temp)
        return
    
    for idx in range(start, len(strings)):
        if not sel[idx]:
            sel[idx] = 1
            search2(temp + [strings[idx]], idx+1)
            sel[idx] = 0

    # for idx, string in enumerate(strings):
    #     if not sel[idx]:
    #         sel[idx] = 1
    #         search2(temp + [string])
    #         sel[idx] = 0

search2([], 0)
# print(len(string_dict))

# for strings in string_dict:
#     print(strings)
# # print(*sorted(string_dict), end='\n')


# 2차원 배열 선언
adj = [[] for _ in range(L+1)]

# 인접리스트 할당
for _ in range(N):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)