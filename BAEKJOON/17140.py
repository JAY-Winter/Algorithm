# 크기 3X3 
# 배열의 인덱스는 1 부터 시작
# 1초마다 아래의 연산 적용
# R 연산 : 배열 A 의 모든 행에 대해서 정렬. 행의 개수 >= 열의 개수
# C 연산 : 배열 A 의 모든 열에 대해서 정렬. 행의 개수 < 열의 개수

# 수 정렬 시, 각각의 수가 몇 번 나왔는 지 알아야함
# 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬
# 그 다음, 배열 A 에 정렬된 결과를 다시 넣어야 함
# 정렬된 결과를 배열에 넣을 땐, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다

#[3, 1, 1]
# 1: 2 , 3 : 1
# [3, 1, 1, 2] -> [2, 1, 3, 1, 1, 2]
from pprint import pprint


def isRorC(arr):
    row = len(arr)
    col = len(arr[0])
    if row >= col:
        return 'R'
    else:
        return 'C'

def check_num(line):
    num_dict = {num: 0 for num in line if num}
    for num in line:
        if num:
            num_dict[num] += 1
    return num_dict

def num_sort(num_dict):
    sorted_dict = sorted(num_dict.items(), key=lambda item: (item[1], item[0]))
    tmp_list = []
    for i in sorted_dict:
        num, cnt = i
        tmp_list.append(num)
        tmp_list.append(cnt)
    return tmp_list

def check_size(arr, mode):
    size = 0
    if mode == 'R':
        for line in arr:
            L = len(line)
            if L > size:
                size = L
    elif mode == 'C':
        for line in arr:
            L = len(line)
    return size

def resize_arr(arr, size):
    temp_arr = [[] for _ in range(len(arr))]
    for idx, line in enumerate(arr):
        if len(line) != size:
            diff = size - len(line)
            for _ in range(diff):
                line.append(0)
        temp_arr[idx] += line
    return temp_arr

def Rsort(arr):
    temp_arr =  [[] for _ in range(len(arr))]
    for idx, line in enumerate(arr):
        temp_line = num_sort(check_num(line))
        temp_arr[idx] += (temp_line)
    return temp_arr

def Csort(arr):
    row = len(arr)
    col = len(arr[0])
    temp_line_list = []
    for i in range(col):
        temp_line = []
        for j in range(row):
            temp_line.append(arr[j][i])
        temp_line = num_sort(check_num(temp_line))
        temp_line_list.append(temp_line)

    max_size = max(len(line) for line in temp_line_list)
    temp_arr = [[0] * len(temp_line_list) for _ in range((max_size))]

    for idx, line in enumerate(temp_line_list):
        diff = max_size - len(line)
        for _ in range(diff):
            temp_line_list[idx].append(0)
    
    for i in range(len(temp_line_list)):
        for j in range(len(temp_line_list[i])):
            temp_arr[j][i] = temp_line_list[i][j]

    return temp_arr


def main():
    r, c, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(3)]
    r -= 1
    c -= 1

    result = -1

    for cnt in range(101):
        try:
            if arr[r][c] == k:
                result = cnt
                break
        except IndexError:
            pass

        if isRorC(arr) == 'R':
            temp_arr = Rsort(arr)
        elif isRorC(arr) == 'C':
            temp_arr = Csort(arr)
        
        max_size = max(len(line) for line in temp_arr)
        resized_arr = resize_arr(temp_arr, max_size)
        arr = resized_arr   
        print(arr)
    return result


print(main())