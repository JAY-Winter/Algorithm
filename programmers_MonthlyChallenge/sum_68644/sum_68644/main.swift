//
//  main.swift
//  sum_68644
//
//  Created by JAEHYEON on 2022/06/22.
//

import Foundation
// 월간 코드 챌린지 시즌1 두 개 뽑아서 더하기
// MARK: - Sol1
var S = Set<Int>()

func solution(_ numbers:[Int]) -> [Int] {
    
    recur(0, numbers)
    
    return S.sorted()
}

func recur(_ idx: Int, _ arr: [Int]) {
    if idx == arr.count {
        return
    }
    
    recur(idx+1, arr)
    
    for i in idx+1 ..< arr.count {
        S.insert(arr[idx] + arr[i])
    }
    
}

// MARK: - Sol2
func solution2(_ numbers:[Int]) -> [Int] {
    var result = Set<Int>()
    
    for i in 0 ..< numbers.count - 1 {
        for j in i+1 ..< numbers.count {
            result.insert(numbers[i]+numbers[j])
        }
    }
    
    
    return result.sorted()
}
