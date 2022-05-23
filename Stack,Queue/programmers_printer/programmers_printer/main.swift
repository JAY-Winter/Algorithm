//
//  main.swift
//  programmers_printer
//
//  Created by JAEHYEON on 2022/05/23.
//

import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var answer = 0
    var priority = priorities
    var targetIndex = location
    

    while true {
        if priority.first! == priority.max() {
            priority.removeFirst()
            answer += 1
            
            if targetIndex == 0 {
                break
            } else {
                targetIndex -= 1
            }
        } else {
            priority.append(priority.removeFirst())
            
            if targetIndex == 0 {
                targetIndex = priority.count - 1
            } else {
                targetIndex -= 1
            }
        }
    }
    print(answer)
    return answer
}

let case1 = solution([2, 1, 3, 2], 2)
let case2 = solution([1, 1, 9, 1, 1, 1], 0)
let case3 = solution([2, 1, 2, 1, 2, 1, 2, 1, 2], 1)
