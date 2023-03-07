//
//  main.swift
//  programmers_farthest_Graph
//
//  Created by JAEHYEON on 2022/06/12.
//

import Foundation

func solution(_ n:Int, _ edge:[[Int]]) -> Int {
    var answer = 0
    
    var visit = [Bool](repeating: false, count: edge.count + 1)
    var nearNode: [[Int]] = Array(repeating: [], count: n + 1) // [[Int]](repeating: , count: )
    
    // 인접리스트 생성
    edge.forEach {
        nearNode[$0[0]].append($0[1])
        nearNode[$0[1]].append($0[0])
    }
    
    print(nearNode)
    
    
    func bfs(idx: Int) {
        for nodes in nearNode {
            for node in nodes {
                if !visit[node] {
                    visit[node] = true
                }
            }
        }
        print(visit)
        
    }
        
    bfs(idx: 1)
    
    

    return 0
}
(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

func solution2(_ n:Int, _ edge:[[Int]]) -> Int {
    var answer1 = 0
    func firstSol() {
        
        var nodeDictionary: Dictionary<Int, [Int]> = [:]
        var farthestNodeSet: Set<Int> = []

        for node in edge {
            var sortedNode = node.sorted()
            nodeDictionary[sortedNode.removeFirst(), default: []].append(contentsOf: sortedNode)
        }
        
        for (a,b) in nodeDictionary {
            if a == 1 {
                for node in b {
                    farthestNodeSet = farthestNodeSet.union(nodeDictionary[node, default: []])
                }
            } else {
                continue
            }
        }
        
        print("nodeDictionary : \(nodeDictionary)")
        print(farthestNodeSet)
        for node in farthestNodeSet {
            for (key, _) in nodeDictionary {
                if node == key {
                    farthestNodeSet.remove(node)
                }
            }
        }
        print(farthestNodeSet)
        answer1 = farthestNodeSet.count
    }
    
    firstSol()
    return answer1
}

// (solution2(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
