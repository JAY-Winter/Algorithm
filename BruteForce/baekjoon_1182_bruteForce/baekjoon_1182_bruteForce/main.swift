//
//  main.swift
//  baekjoon_1182_bruteForce
//
//  Created by JAEHYEON on 2022/05/29.
//

import Foundation



let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let S = input[1]
let arr = readLine()!.split(separator: " ").map { Int($0)! }
var sum = 0

print(N, S)
print(arr)





var visited = Array(repeating: false, count: 21)
print(visited)

var cnt = 0 

func dfs(_ depth: Int, _ start: Int) {
    // 여기서 depth >= 1 는 뭘까?
    if sum == S && depth >= 1 {
        cnt += 1 // 결과 +1
    }
    
    for i in start ..< N {
        
    }
    
}
