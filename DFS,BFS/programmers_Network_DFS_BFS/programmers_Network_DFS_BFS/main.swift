//
//  main.swift
//  programmers_Network_DFS_BFS
//
//  Created by JAEHYEON on 2022/06/07.
//

import Foundation


func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    
    var visited = [Bool](repeating: false, count: n)
    var answer = 0
    
    func dfs(_ idx: Int) {
        visited[idx] = true // 방문한 노드에 대해서 방문처리를 해줌
        
        for i in 0 ..< n {
            // computers[i][j] 가 1 이고, 방문처리 되어있지 않다면
            // 즉, 연결되어있는데 방문하지 않은 것이라면 ~
            // 이에 대해서 재귀처리
            if computers[idx][i] == 1 && visited[i] == false {
                dfs(i)
            }
        }
    }

    for i in 0 ..< n {
        // 여기서 dfs(i) 가 실행되었다는 것 자체가 하나의 그룹이 생성되었다는 의미
        if visited[i] == false { // !visited[i] 와 동일한 구조
            dfs(i)
            answer += 1
        }
    }
    
    
    return answer
}

// case1
print(solution(3,
               [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 1]
               ]))

// case2
print(solution(3,
               [
                [1, 1, 0],
                [1, 1, 1],
                [0, 1, 1]
               ]))
