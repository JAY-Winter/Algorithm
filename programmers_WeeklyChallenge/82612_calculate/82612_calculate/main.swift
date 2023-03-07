//
//  main.swift
//  82612_calculate
//
//  Created by JAEHYEON on 2022/06/16.
//

import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var answer:Int64 = -1

    var sum = 0
    var result: Int64 = 0
    
    func dfs(_ idx: Int) {
        sum += price * idx
        
        if idx == count {
            return
        }
        
        dfs(idx + 1)
    }
    
    dfs(1)
    
    if money > sum {
        result = 0
    } else {
        result = Int64(sum - money)
    }
    
    answer = result
    
    return answer
}



