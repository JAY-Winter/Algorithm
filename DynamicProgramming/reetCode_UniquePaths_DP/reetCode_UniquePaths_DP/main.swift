//
//  main.swift
//  reetCode_UniquePaths_DP
//
//  Created by JAEHYEON on 2022/06/02.
//

import Foundation




/// TESTING
func uniquePaths(_ m: Int, _ n: Int) -> Int {
    var result = 0
    // 값을 momoziation
    var dp = Array(repeating: Array(repeating: 1, count: m), count: n)
    
    for i in 1 ..< dp.count {
        for j in 1 ..< dp[i].count {
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        }
    }
    // stride ... 사용 권장
    
    result = dp[n-1][m-1] // (6,2)
    return result
}

let sol = uniquePaths(3, 7)


let case1 = uniquePaths(3,7)
print(case1)

let case2 = uniquePaths(1, 2)
print(case2)


