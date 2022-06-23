//
//  main.swift
//  reverse_68935
//
//  Created by JAEHYEON on 2022/06/22.
//

import Foundation

func solution(_ n:Int) -> Int {
    
    let a = String(n, radix: 3)
    let b = String(a.reversed())
    
    let result = Int(b, radix: 3)!
    
    return result
}

// solution(45)
print("---")
// solution(125)

