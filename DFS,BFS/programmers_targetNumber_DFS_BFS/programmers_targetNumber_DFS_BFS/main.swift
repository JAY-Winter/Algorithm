//
//  main.swift
//  programmers_targetNumber_DFS_BFS
//
//  Created by JAEHYEON on 2022/06/06.
//

import Foundation

// target Number
func solution(_ numbers:[Int], _ target:Int) -> Int {
    var answer: Int = 0
    
    // 주어진 배열로 타겟 넘버를 만들어야함
    func dfs(_ idx: Int, _ sum: Int) {
        // numbers.count - 1 의 이유는 idx 는 0 부터 시작
        // idx 가 3일 때, 아래 재귀구조에서 numbers[3 + 1] ...
        // numbers.count 로만 작성하면 out of range error 발생
        if idx == numbers.count - 1 {
            if sum == target {
                answer += 1
            }
            return
        }

        dfs(idx + 1, sum + numbers[idx + 1])
        dfs(idx + 1, sum - numbers[idx + 1])
    }
    // idx = -1 인 이유 : -1 이어야 첫 번째 재귀에서 dfs(0, 0 + 1) 로 시작함
    dfs(-1, 0)

    return answer
}

// print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))

// 스택과 큐 .......
// 스택으로 다시 풀어보자 !_!

// 이분탐색은 쉬운데
// 이분탐색을 어떻게 써볼까.. "판단"하는게 어렵다 ~

// 키워드
// lower&upper Bound
// >> 이분탐색을 활용한 알고리즘이다
// 스위프트에서는 없다 구현을 해야한다
// 이분탐색트리 공부해두면 좋다~
