//
//  main.swift
//  86971_divied
//
//  Created by JAEHYEON on 2022/06/18.
//

import Darwin

// let wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
let wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
// let n = 9
let n = 7

var answer = 0

func makeAdjacencyList(_ nodes: [[Int]], _ n: Int) -> [[Int]] {
    var nearNode = [[Int]](repeating: [], count: n + 1)
    
    wires.forEach {
        nearNode[$0[0]].append($0[1])
        nearNode[$0[1]].append($0[0])
    }
    print(nearNode)
    
    return nearNode
}


let nearNode = makeAdjacencyList(wires, n)
var maxNode = -1 // 앞 부분의 가장 많은 노드의 개수
var maxIdx = 0 // maxNode 의 번호

for node in stride(from: 1, to: nearNode.count, by: 1) {
    if nearNode[node].count > maxNode {
        maxNode = nearNode[node].count
        maxIdx = node
    }
}

print(maxIdx, maxNode)

func solution(_ n:Int, _ wires:[[Int]]) -> Int {
    bfs(0, maxIdx)
    
    return answer
}

var visit = [Bool](repeating: false, count: n + 1)

var maxCount = -1

var 노드별전력개수 = [Int: Int]()

func bfs(_ idx: Int, _ maxIdx: Int) {
    visit[maxIdx] = true
    var count = 0
    
    if count == nearNode[maxIdx].count { return }
    print("maxIdx : \(maxIdx)")
    
    for node in nearNode[maxIdx] {
        if !visit[node] {
            count += 1
            print(count)
            bfs(idx, node)
            // visit[node] = false
        }
    }
    
    
    /// 간선을 하나씩 끊은 다음 
    
    
    
    
    
    
    
    
    
    
    // visit[maxIdx] = true
    // var now = 0
    // for node in nearNode[maxIdx] {
    //
    //     if now == nearNode[maxIdx].count { return }
    //
    //     print("node : \(node)")
    //     if !visit[node] {
    //         visit[node] = true
    //
    //         bfs(idx + 1, node)
    //         count += 1
    //     }
    //
    //     now += 1
    // }
}

solution(n, wires)

/*
 1: [2]
 2: [1,7]
 3: [4,7]
 4: [3,5]
 5: [4]
 6: [7]
 7: [2,3,6]
 
 7의 인접노드을 방문순회
 
 2를 방문
 
 */
