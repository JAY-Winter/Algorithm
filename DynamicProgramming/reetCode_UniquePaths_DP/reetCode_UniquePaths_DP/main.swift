//
//  main.swift
//  reetCode_UniquePaths_DP
//
//  Created by JAEHYEON on 2022/06/02.
//

import Foundation

func uniquePaths(_ m: Int, _ n: Int) -> Int {
    var result = 0
    var dp = Array(repeating: Array(repeating: 1, count: m), count: n)
    dp[0][0] = 1
    dp[n-1][m-1] = 1

    
    

    for i in 1 ..< dp.count {
        for j in 1 ..< dp[i].count {
            print(i, j)
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        }
    }

    
    result = dp[n-1][m-1]
    return result
}


let case1 = uniquePaths(3,7)
print(case1)

let case2 = uniquePaths(1, 2)
print(case2)

