//
//  main.swift
//  DFS_study_1
//
//  Created by JAEHYEON on 2022/06/06.
//

import Foundation

let graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

var visited = [Bool](repeating: false, count: 9)

func dfs(_ v: Int) {
    visited[v] = true
    print(v)
    for i in graph[v] {
        if !visited[i] {
            dfs(i)
        }
    }
}

dfs(1)
