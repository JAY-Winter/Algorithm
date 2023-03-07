//
//  main.swift
//  repeat_70129
//
//  Created by JAEHYEON on 2022/06/22.
//

import Foundation


func solution(_ s:String) -> [Int] {
    
    let c = s.map { Int(String($0))! }
    // print(c)
    
    let x = c.filter { $0 != 0 }
    print(x)
    
    var str = ""
    
    for i in x {
        str += String(i)
    }
    print(str)
        
    let result = Int(str, radix: 2)!
    print(result)
    
    return []
}

// 월간 코드 챌린지 시즌1 - 이진 변환 반복하기
func solution2(_ s:String) -> [Int] {
    var result = [0,0]
    var S = s
    var c = 0 // 제거되는 0의 개수

    func recur(_ idx: Int, _ S: inout String) {
        let R = idx // 반복 횟수
        // print(R, c)
        result[0] = R
        result[1] = c
        
        if S == "1" {
            return
        }

        // 0 이 제거된 문자열
        let x = S.map { String($0) }.filter {
            if $0 == "0" {
                c += 1
            }
            return $0 != "0"
        }
        // 0이 제거된 문자열의 길이
        let k = x.joined().count

        var j = String(k, radix: 2)

        recur(idx + 1, &j)
    }
    
    recur(0, &S)
    
    return result
}




print(solution2("110010101001"))
print(solution2("01110"))
print(solution2("1111111"))
