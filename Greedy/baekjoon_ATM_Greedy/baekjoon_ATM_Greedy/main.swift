//
//  main.swift
//  baekjoon_ATM_Greedy
//
//  Created by JAEHYEON on 2022/05/31.
//

import Foundation

// let N = 5
// var Pi = [3,1,4,3,2]
// 필요한 시간의 합의 최솟값은 돈을 인출하는데 걸리는 시간이 작은 순대로 정렬되어있을 때다.
// 1,2,3,3,4
// 1
// 1 + 2
// 1 + 2 + 3
// 1 + 2 + 3 + 3
// 1 + 2 + 3 + 3 + 4


// MARK: - 실제 논리부분

let Nn = readLine() // 코드에서 사실 쓰이진 않음, 어떻게 활용하면 좋을까?
let arr = readLine()!.split(separator: " ").map { Int($0)! }.sorted()
var sum = 0

// 문제를 정리해봤을 때, 단순반복구조기에 재귀구조를 이용해보았음
func atm(_ N: Int) {
    // 재귀 탈출구조 : 배열 개수만큼 재귀를 반복했을 때
    if N == arr.count {
        return
    }
    // 재귀때 마다 count 하는 배열의 index 개수가 늘어남
    for i in 0 ... N {
        sum += arr[i]
    }
    // 재귀
    atm(N+1)
    // print(N) 을 찍으면서 stack 부분에서 어떻게 pop 되면서 나오는지 확인할 수 있음
    print(N)
}

atm(0)
print(sum)


