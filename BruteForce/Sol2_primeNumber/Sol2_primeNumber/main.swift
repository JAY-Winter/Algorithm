//
//  main.swift
//  Sol2_primeNumber
//
//  Created by JAEHYEON on 2022/06/11.
//

import Foundation

func solution(_ numbers:String) -> Int {
    
    // let N = numbers.count
    // let convertedNumbersToArray = numbers.map { Int((String($0)))! }
    // var visit = [Bool](repeating: false, count: N+1)
    //
    //
    // func isPrime(_ N: Int) -> Bool {
    //     if N == 1 || N == 0 { return false }
    //
    //     return false
    // }
    //
    // func recur(_ idx: Int, _ str: String) {
    //     print(str)
    //     if idx == N {
    //         return
    //     }
    //
    //     recur(idx + 1, str + convertedNumbersToArray[idx])
    // }

    //
    // var appendArr: [Int] = []
    // var answer: [[Int]] = []
    
    
    // func recur2(_ now: Int) {
    //     if now == N {
    //         answer.append(appendArr)
    //         return
    //     }
    //
    //     for i in 1 ... N {
    //         if visit[i] == false {
    //             visit[i] = true
    //             print(convertedNumbersToArray)
    //             print(appendArr)
    //             appendArr.append(convertedNumbersToArray[i])
    //             recur2(now + 1)
    //             appendArr.removeFirst()
    //             visit[i] = false
    //         }
    //     }
    //     print(answer)
    // }
    //
    // recur2(1)

    let nums = numbers.map { String($0) }
    var numSet: Set<Int> = []
    
    
    func permutation() {
        
        print(nums)
        
        
        
        
        
    }
    
    permutation()
    
    
    return 0
}

solution("17")
print("---------------")
solution("011")
