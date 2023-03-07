//
//  main.swift
//  BinaraySearch_study
//
//  Created by JAEHYEON on 2022/06/09.
//

import Foundation

func binarySearch(array: Array<Int>, target: Int, start: Int, end: Int) -> Int? {
    
    if start > end {
        return nil
    }
    
    let mid = (start + end) / 2
    print(mid)
    
    if array[mid] == target {
        return mid
    }
    
    else if array[mid] > target {
        return binarySearch(array: array, target: target, start: start, end: mid - 1)
    }
    
    else {
        return binarySearch(array: array, target: target, start: mid + 1, end: end)
    }
}

let target = 9
let array = [1,3,5,7,9,11,13,15,17,19]
let n = array.count

let result = binarySearch(array: array, target: target, start: 0, end: n - 1)

if result == nil {
    print("원소가 존재하지 않습니다.")
} else {
    print(result ?? 0)
}
