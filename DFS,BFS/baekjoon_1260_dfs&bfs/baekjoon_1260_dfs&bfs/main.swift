//
//  main.swift
//  baekjoon_1260_dfs&bfs
//
//  Created by JAEHYEON on 2022/06/14.
//

import Foundation

// 인접리스트 생성 함수
func generateAdjacencyList(with array: [[Int]]) -> [[Int]] {
    
    // var adjacencyList: [[Int]] = []
    var adjacencyList = [[Int]](repeating: [], count: array.count)
    
    
    array.forEach {
        adjacencyList[$0[0]].append($0[1])
        adjacencyList[$0[1]].append($0[0])
    }
    
    return adjacencyList
}

func solution() {

    let input = readLine()!.split(separator: " ").map { Int($0) }
    let N = input[0]!
    let M = input[1]!
    let V = input[2]!
    
    var inputArray: [[Int]] = []
    
    for _ in 0 ..< M {
        let splitInput = readLine()!.split(separator: " ").map{ Int($0)! }
        inputArray.append(splitInput)
    }
    
    let nearNode = generateAdjacencyList(with: inputArray)
    
    var Q: [Int] = []
    var visit = [Bool](repeating: false, count: N + 1)
    
    func bfs(_ idx: Int) {
        Q.append(idx)
        visit[idx] = true
        
        var now = 0

        while now != Q.count {
            now += 1
            for node in nearNode[now] {
                if !visit[node] {
                    visit[node] = true
                    Q.append(node)
                }
            }
        }
        
    }
    bfs(V)
    
    Q.forEach {
        print($0, terminator: " ")
    }
}

solution()





// MARK: - BFS test

var Q: [Int] = []

func testBfs(_ idx: Int) {
    let nearNode = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
    var visit = [Bool](repeating: false, count: 8 + 1)
    var now = 0
    
    Q.append(idx)
    visit[idx] = true
    // (now, Q.count) : (0, 1) > (1, 4)
    
    while now != Q.count {
        
        now += 1
        print(now, Q.count)
        for node in nearNode[now] {
            if !visit[node] {
                visit[node] = true
                Q.append(node)
            }
        }
        print(Q)
    }
    
}

// testBfs(1)
