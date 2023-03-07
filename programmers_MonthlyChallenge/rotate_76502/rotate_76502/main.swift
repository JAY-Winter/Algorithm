//
//  main.swift
//  rotate_76502
//
//  Created by JAEHYEON on 2022/06/26.
//

import Foundation

// ( [ { ) } ]
func solution(_ s:String) -> Int {
    var answer = 0
    var str = s.map { String($0) }

    let C1 = (L: "[", R: "]")
    let C2 = (L: "(", R: ")")
    let C3 = (L: "{", R: "}")
    print(str)
    var stack = [String]()
    //
    // if str.contains(C1.L) && str.contains(C2.L) && str.contains(C3.L) {
    //     stack.append((C1.L))
    //     stack.append((C2.L))
    //     stack.append((C3.L))
    // } else {
    //     print(" 1")
    // }
    
    for S in str {
        if S == C1.L || S == C2.L || S == C3.L {
            stack.append(S)
        } else {
            // print("no")
            if S == C1.R { print(C1.L, S) }
            
        }
    }
    
    // var stack2 = [String]()
    //
    // for S in str {
    //     print(S)
    //     stack2.append(S)
    //
    //     for s in stack2 {
    //
    //     }
    // }
    
    return answer
}



solution("[](){}")

// for _ in stride(from: start, to: end, by: 1) {
//     var stack = [Character]()
//     for idx in str {
//
//         stack.append(idx)
//
//     }
//     str.append(str.remove(at: 0))
// }
