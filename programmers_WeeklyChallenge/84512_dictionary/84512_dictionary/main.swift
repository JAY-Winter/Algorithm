//
//  main.swift
//  84512_dictionary
//
//  Created by JAEHYEON on 2022/06/16.
//

import Foundation

let col = ["A", "E", "I", "O", "U"]

func solution(_ word: String) -> Int {
    dfs(word, "", &now)
    now = 0
    return answer
}

var str = ""
var now = 0
var answer = 0

func dfs(_ word: String, _ idx: String, _ now: inout Int) {
    if idx.count > 5 {
        return
    }

    for i in col {
        let doc = idx + i
        
        if (doc).count > 5 {
            return
        }
        
        now += 1

        if doc == word {
            print(doc, now)
            answer = now
        }
        dfs(word, doc, &now)
    }
}

print(solution("AAAAE"))

print(solution("AAAE"))

print(solution("I"))

print(solution("EIO"))

