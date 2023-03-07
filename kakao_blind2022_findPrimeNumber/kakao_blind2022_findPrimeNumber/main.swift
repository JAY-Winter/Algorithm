//
//  main.swift
//  kakao_blind2022_findPrimeNumber
//
//  Created by JAEHYEON on 2022/06/13.
//

import Foundation

func isPrime(_ P: Int) -> Bool {
    var idx = 2
    
    while (idx * idx) <= P {
        if P % idx == 0 {
            return false
        }
        idx += 1
    }
    return true
}

func solution(_ n:Int, _ k:Int) -> Int {
    var answer = 0
    
    let number = String(n, radix: k)
    print("number : \(number)")
    
    let splitedNumber = number.split(separator: "0").map { Int($0)! }
    print("splitedNumber : \(splitedNumber)")
    
    for number in splitedNumber {
        
        if isPrime(number) && number > 1 {
            print("number : \(number)")
            answer += 1
        }
    }
    
    return answer
}

print("answer: \(solution(437674, 3))")
print("--------------------")
print("answer: \(solution(110011, 10))")
