//
//  main.swift
//  baekjoon_1149_DP
//
//  Created by JAEHYEON on 2022/06/02.
//

import Foundation

let N = Int(readLine()!)!
var dp: [[Int]] = []
// 1. 입력받은 N 만큼 반복해서 RGB 값을 입력 후 이를 dp arr 에 append
for _ in 0 ..< N {
    let rgb = readLine()!.split(separator: " ").map { Int($0)! }
    dp.append(rgb)
}


// 2. dp.count 만큼 반복, 이때 1부터 시작하는 이유는 dp[i][0] 값 즉, 1번째 행의 index 를 각각의 RGB 초기값으로 잡을 것이기 때문
for i in 1 ..< dp.count {
    // 이전 행의 다른 색깔끼리 비교...
    // R 값
    // print("변경 전 : \(dp[i][0]), \(dp[i][1]), \(dp[i][2])")
    dp[i][0] = dp[i][0] + min(dp[i-1][1], dp[i-1][2])
    // G 값
    dp[i][1] = dp[i][1] + min(dp[i-1][0], dp[i-1][2])
    // B 값
    dp[i][2] = dp[i][2] + min(dp[i-1][0], dp[i-1][1])
    // print("변경 후 : \(dp[i][0]), \(dp[i][1]), \(dp[i][2])")
}

// dp.forEach { dp in
//     print(dp)
// }
print(min(min(dp[N-1][0], dp[N-1][1]), dp[N-1][2]))
