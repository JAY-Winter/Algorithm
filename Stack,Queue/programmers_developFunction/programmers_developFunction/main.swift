//
//  main.swift
//  programmers_developFunction
//
//  Created by JAEHYEON on 2022/05/21.
//

import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var progresses = progresses
    var Q: [Int] = []
    var speedPerProgress: [Int: Int] = [:]
    var num: Int = 0
    var result: [Int] = []
    
    for (progress, speed) in zip(progresses, speeds) {
        speedPerProgress[progress] = speed
    }
    
    for progress in 0 ..< progresses.count {
        var count: Int = 0
        let program = progresses[progress]
        while progresses[progress] < 100 {
            progresses[progress] += speedPerProgress[program, default: 0]
            count += 1
        }
        Q.append(count)
    }
    print("dayToCompleteWork : \(Q)")
    
    while !Q.isEmpty {
        var cnt = 0
        cnt += 1
        num = Q.removeFirst()
        while !Q.isEmpty && num >= Q.first! {
            cnt += 1
            Q.removeFirst()
        }
        result.append(cnt)
    }
    print("result : \(result)")
    return result
}

let case1 = solution([93, 30, 55], [1, 30, 5])
let case2 = solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
