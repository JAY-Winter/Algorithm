//
//  main.swift
//  baekjoon_1788_DP
//
//  Created by JAEHYEON on 2022/06/02.
//

import Foundation


var sum = 0

func fibo(_ N: Int) -> Int {
    if N == 0 {
        return 0
    }
    
    if N == 1 {
        return 1
    }
    if N == -1 {
        return -1
    }
    
    if N > 1 || N <= 1 {
        sum = fibo(N-1) + fibo(N-2)
        print(N, sum)
        return sum
    }
    return sum
}

// print(fibo(7))
// print(fibo(-7))
print(fibo(0))
print(fibo(-1))
print(fibo(-2))
