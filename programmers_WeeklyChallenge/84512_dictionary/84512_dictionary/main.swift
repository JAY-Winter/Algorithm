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
    // 5 글자수 제한
    if idx.count > 5 {
        return
    }
    
    for i in col {
         // "" + "A"
        let doc = idx + i
        
        print(doc)
        if doc.count > 5 {
            return
        }
        
        now += 1
        // 매개변수 word 와 만들어진 doc 가 일치할 때
        if doc == word {
            print(doc, now)
            answer = now
        }
        
        dfs(word, doc, &now)
    }
}

print(solution("AAAAE"))

// print(solution("AAAE"))

// print(solution("I"))

// print(solution("EIO"))

