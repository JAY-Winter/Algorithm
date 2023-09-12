arr = [6, 5, 3, 1, 8, 7, 2, 4]

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    print(left)
    print(right)
    print()
    merged_arr = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    # print(merged_arr)

    return merged_arr

merge_sort(arr)