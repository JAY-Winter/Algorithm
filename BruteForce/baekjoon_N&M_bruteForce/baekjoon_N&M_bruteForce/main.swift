//
//  main.swift
//  baekjoon_N&M_bruteForce
//
//  Created by JAEHYEON on 2022/05/30.
//

import Foundation

let NM = readLine()!.split(separator: " ").map { Int($0)! }
let N = NM[0] // 자연수 N
let M = NM[1] // M개를 고르는 경우
var visit: [Bool] = [Bool](repeating: false, count: N + 1) // N + 1 인 이유는 1.. 부터 하기 위함
var appendArr: [Int] = []
var answer: [[Int]] = []

func recur(_ now: Int) {
    if now == M {
        answer.append(appendArr)
        return
    }
    
    for i in 1 ... N {
        if visit[i] == false {
            visit[i] = true
            appendArr.append(i)
            recur(now + 1)
            appendArr.removeFirst()
            visit[i] = false
        }
    }
    print(answer)
}

recur(0)


























//
// var answer: [[Int]] = []
// var appendArr: [Int] = []
// var visit: [Bool] = [Bool](repeating: false, count: N + 1)
// func recur(_ now: Int) {
//     if now == M {
//         answer.append(appendArr)
//         return
//     }
//     for i in 1...N {
//         if visit[i] == false {
//             visit[i] = true
//             appendArr.append(i)
//             recur(now + 1)
//             appendArr.removeLast()
//             visit[i] = false
//         }
//     }
// }
// recur(0)
// answer.forEach {
//     $0.forEach {
//         print($0, terminator: " ")
//     }
//     print()
// }
//
//

