//
//  main.swift
//  baekjoon_2750_sort
//
//  Created by JAEHYEON on 2022/05/26.
//

import Foundation

// func makeArr() -> [Int] {
//     let N: Int = Int(readLine()!)!
//
//     var array: [Int] = []
//
//     for _ in 0..<N {
//         let x: Int = Int(readLine()!)!
//         array.append(x)
//     }
//
//     return array
//
// }
//
// let arr = makeArr()
//
// func quickSort(_ array: [Int]) -> [Int] {
//     if array.count < 2 {
//         return array
//     }
//
//     let P = array[0]
//     let smaller = array.filter{ $0 < P }
//     let bigger = array.filter{ $0  > P }
//
//     return quickSort(smaller) + [P] + quickSort(bigger)
// }
//
// func sortLibrary(_ array: [Int]) -> [Int] {
//     array.sorted()
// }
//
// let result = quickSort(arr)
// let result2 = sortLibrary(arr)
//
// for i in result {
//     print(i)
// }
//
// for j in result2 {
//     print(j)
// }
//
//
// // "탈출 조건" 을 먼저 쓰는 연습을 하자..!
// // 어디서 탈출이 될까 설계
// // 설계....

// BOJ 2751 수 정렬하기 2 (오름차순)
// MergeSort
// 가장 작은 부분배열까지 쪼갠 후 합치는 과정에서 정렬


// 쪼개는 함수
func mergeSort(_ arr: [Int]) -> [Int] {
    if arr.count < 2  { return arr }
    let mid = arr.count / 2
    
    let leftArr = Array(arr[0..<mid])
    let rightArr = Array(arr[mid..<arr.count])
    
    return merge(leftArr: mergeSort(leftArr), rightArr: mergeSort(rightArr))
}

// 합치는 함수
func merge(leftArr: [Int], rightArr: [Int]) -> [Int] {
    var sortedArr = [Int]()
    var left = 0
    var right = 0
    
    while left < leftArr.count && right < rightArr.count {
        if leftArr[left] <= rightArr[right] {
            sortedArr.append(leftArr[left])
            left += 1
        } else {
            sortedArr.append(rightArr[right])
            right += 1
        }
    }
    
    sortedArr.append(contentsOf: leftArr[left..<leftArr.count])
    sortedArr.append(contentsOf: rightArr[right..<rightArr.count])
    
    return sortedArr
}

fileprivate let size = Int(readLine()!)!
fileprivate var arr = Array(repeating: 0, count: size)

for i in 0..<size {
    arr[i] = Int(readLine()!)!
}

fileprivate let sorted = mergeSort(arr)
sorted.forEach { print($0) }
