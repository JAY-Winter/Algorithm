//
//  main.swift
//  reetCode_Search_a_2D Matrix_II_binaraySearch
//
//  Created by JAEHYEON on 2022/06/09.
//

import Foundation

let matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]

let target = 5

var resultArr = [Bool](repeating: false, count: matrix.count)

for i in matrix {

    func binarySearch(array: [Int], start: Int, end: Int) -> Int {
        if start > end {
            return 0
        }

        let mid = (start + end) / 2

        if array[mid] == target {
            return 0
        }


        if array[mid] > target {
            return binarySearch(array: i, start: start, end: mid - 1)
        }

        else if array[mid] < target {
            return binarySearch(array: i, start: mid + 1, end: end)
        }

        return 0
    }
    
    if binarySearch(array: i, start: 0, end: i.count) == 0 {
        resultArr.append(false)
    } else {
        resultArr.append(true)
    }
}

print("resultArr : \(resultArr)")

if resultArr.contains(true) {
    print(true)
} else {
    print(false)
}


















class Solution {

    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        var result: Bool = false

        var resultArr = [Bool](repeating: false, count: matrix.count)

        for index in matrix {
            func binarySearch(array: [Int], start: Int, end: Int) -> Int? {
                // 탐색하려고 하는 범위에 데이터가 존재하지 않는 것
                if start > end {
                    return nil
                }
                // 중간 값 선언
                let mid = (start + end) / 2
                
                // 배열의 중간값이 타겟과 동일하면 mid 위치 return
                if array[mid] == target {
                    return mid
                }


                if array[mid] > target {
                    return binarySearch(array: index, start: start, end: mid - 1)
                }

                else if array[mid] < target {
                    return binarySearch(array: index, start: mid + 1, end: end)
                }

                return 0
            }

            if binarySearch(array: index, start: 0, end: index.count) == 0 {
                resultArr.append(false)
            } else {
                resultArr.append(true)
            }
        }
        
        
        
        if resultArr.contains(true) {

            result = true
        } else {
            result = false
        }

        return result
    }
}
