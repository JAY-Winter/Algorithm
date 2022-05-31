//
//  main.swift
//  quickSort
//
//  Created by JAEHYEON on 2022/05/26.
//

import Foundation

// MARK: - Solution1 Pivot 중간 값 이용

var arr = [3,9,4,7,5,0,1,6,8,2]

func quickSort(_ arr: inout [Int], _ start: Int, _ end: Int) {
    if start > end { return }
    
    var mid = (start + end) / 2
    let pivot: Int = arr[mid]
    var left = start
    var right = end
    
    while isDeviate(&arr, left, right) {
        while left <= end && arr[left] < pivot {
            left += 1
        }
        while right > start && arr[right] > pivot {
            right -= 1
        }
        print(left, right)
        
        if left <= right {
            swap(&arr, &left, &right)
        } else {
            swap(&arr, &right, &mid)
        }
    }
    print(arr)
    
    quickSort(&arr, start, right - 1) // 앞부분 담당
    quickSort(&arr, right + 1, end) // 뒷부분 담당
}

func swap(_ arr: inout [Int], _ start: inout Int, _ end: inout Int) {
    let temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
}

// 어긋나는지 확인 : start 위치가 end 위치보다 클 때 엇갈리는 것이므로 멈춰야함
func isDeviate(_ arr: inout [Int], _ start: Int, _ end: Int) -> Bool {
    return start >= end ? false : true
}

quickSort(&arr, 0, arr.count - 1)

// MARK: - Solution2 filter 이용

func quickSort2(array: [Int]) -> [Int] {
    print(array)
    if array.count < 2 {
        return array
    } else {
        let P = array[0]
        let smaller = array.filter { $0 < P }
        let bigger = array.filter { $0 > P}
        return quickSort2(array: smaller) + [P] + quickSort2(array: bigger)
    }
}

// MARK: - Solution1 복습

func quickSort3(_ arr: inout [Int], _ left: Int, _ right: Int) {
    var start = left
    var end = right
    var mid = (left + right) / 2
    var pivot = arr[mid]
    
    if start > end { return }
    
    
    // 처음에 if start > end { return } 으로 탈출구 마련해놨는데 이 조건이 필요하나?
    // while start < end && start < pivot { }
    
    while start < pivot {
        start += 1
    }
    
    while end > pivot {
        end -= 1
    }
    
    
}

func swap(_ arr: inout [Int], _ left: Int, _ right: Int) {
    let temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
}


