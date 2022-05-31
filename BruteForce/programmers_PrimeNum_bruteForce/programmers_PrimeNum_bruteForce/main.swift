//
//  main.swift
//  programmers_PrimeNum_bruteForce
//
//  Created by JAEHYEON on 2022/05/29.
//

import Foundation



func solution(_ numbers:String) -> Int {
    
    var result: [[Int]] = []
    var arr = numbers.map { Int(String($0))! }

    func joinedArr(_ arr: [[Int]]) {
        for i in 0 ..< arr.count {
            print(arr[i])
        }
    }
    print(arr)

    func permutation(_ k: Int) {
        if k == arr.count {
            return
        }
        
        for i in k ..< arr.count {
            arr.swapAt(k, i)
            permutation(k+1)
            arr.swapAt(k, i)
        }
    }
    
    

    return 0
}


