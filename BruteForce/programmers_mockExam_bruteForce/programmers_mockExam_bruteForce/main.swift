//
//  main.swift
//  programmers_mockExam_bruteForce
//
//  Created by JAEHYEON on 2022/05/29.
//

import Foundation

// solution([1,2,3,4,5])
let first = [1, 2, 3, 4, 5]
let second = [2, 1, 2, 3, 2, 4, 2, 5]
let third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

func solution(_ answers:[Int]) -> [Int] {
    var result: [Int] = []
    var cnt: Int = 0
    
    for answer in answers {
        var tmp = 0
        for i in tmp ..< first.count {
            print(first[i])
            
            if answer == first[tmp] {
                cnt += 1
                break
            } else {
                break
            }
        }
    }
    

    
    
    
    return []
}

print(solution([1,2,3,4,5]))
