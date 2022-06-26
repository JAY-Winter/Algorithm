//
//  main.swift
//  splitArray_87390
//
//  Created by JAEHYEON on 2022/06/26.
//

import Foundation


// 미친 시간 초과...!
func solution(_ n:Int, _ left:Int64, _ right:Int64) -> [Int] {
    //      0       1         2         3       4         5        6        7       8
    // 1: [0,0] 2: [0,1]  3: [0,2] 2: [1,0] 2: [1,1] 3: [1,2] 3: [2,0] 3: [2,1] 3: [2,2]
    //                        3         2       2       3
    
    var array = [Int]()
    
    for idx in 0 ..< n*n {
        
        var xy = (x: 0, y: 0)
        xy.x = idx / n
        xy.y = idx % n
        
        let max = max(xy.x, xy.y)
        
        array.append(max+1)
    }
    
    var answer = array[Int(left)...Int(right)].map { $0 }

    return answer
}

print(solution(3, 2, 5))
print(solution(4, 7, 14))
