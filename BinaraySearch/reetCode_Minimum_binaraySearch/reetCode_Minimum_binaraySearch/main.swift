//
//  main.swift
//  reetCode_Minimum_binaraySearch
//
//  Created by JAEHYEON on 2022/06/10.
//

import Foundation


// func findMin(_ nums: [Int]) -> Int {
//
//     let L = 0
//     let R = nums.count - 1
//
//     while L <= R {
//         if nums[L] <= nums[R] {
//             return nums[L]
//         }
//         let M = (L + R) / 2
//
//         if nums[M] >= nums[L] {
//
//         }
//     }
//
//
//     return 0
// }
//


func findMin(_ nums: [Int]) -> Int {
    var start = 0
    var end = nums.count - 1

    func binarySearch(_ array: [Int], start: inout Int, end: inout Int) -> Int? {
        let mid = (start + end) / 2

        if mid == start {
            return array[mid]
        }

        if array[mid] > array[start] {
            start = mid + 1
            return binarySearch(array, start: &start, end: &end)
        } else {
            end = mid
            return binarySearch(array, start: &start, end: &end)
        }
        return nil
    }
    
    print(binarySearch(nums, start: &start, end: &end))
    
    return 0
}


findMin([3,4,5,1,2])
findMin([4,5,6,7,0,1,2])
// [1,2,3,4,5]
// [4,5,1,2,3]
// [1,2,3,4]
// 채은최공
