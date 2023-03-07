//
//  main.swift
//  baekjoon_2667_BFS
//
//  Created by JAEHYEON on 2022/06/08.
//

import Foundation

let N = Int(readLine()!)!

var map: [[Character]] = []
var visit: [[Bool]] = []


// [상, 하, 좌, 우] 이건가?
let dx = [0, 0, 1, -1]
let dy = [1, -1, 0, 0]

func input() {
    for _ in 0 ..< N {
        let str = readLine()!
        map.append(Array(str))
        visit.append([Bool](repeating: false, count: N))
    }
}

func bfs(_ x: Int, _ y: Int) -> Int {
    var q: [(x: Int, y: Int)] = [(x, y)]
    
    visit[x][y] = true
    
    var front = 0 // 위치를 나타내는 변수
    var ret = 1 // return : 집이 있다를 표시
    
    func isEmpty() -> Bool {
        front == q.count // 이 부분에 대해서 생각해봐야함
    }
    
    while !isEmpty() {
        let now = q[front] // queue 에서 front 가 가르키는 곳
        front += 1 // 뒤로 한 칸 감
        
        for i in 0 ..< 4 {
            let newX = now.x + dx[i]
            let newY = now.y + dy[i]
            
            // 제한 조건
            if newX < 0 || newX >= N || newY < 0 || newY >= N { continue }
            if visit[newX][newY] { continue }
            if map[newX][newY] == "0" { continue }
            // 위 제한 조건 통과 한 newX, newY
            visit[newX][newY] = true
            ret += 1
            q.append((newX, newY))
        }
    }
    return ret
}

input()

var count = 0
var answer: [Int] = []

for i in 0 ..< N {
    for j in 0 ..< N {
        if map[i][j] == "1", visit[i][j] == false {
            answer.append(bfs(i, j))
            count += 1
        }
    }
}

print(count)

answer.sort()
answer.forEach {
    print($0)
}


