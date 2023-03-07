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
    
    // 반복문 자체가 말이 안 됨 .. . ..
    
    // 10^14
    for idx in 0 ..< n*n {
        
        var xy = (x: 0, y: 0)
        xy.x = idx / n
        xy.y = idx % n
        
        // let max = max(xy.x, xy.y)
        var max = 0
        
        if idx >= left && idx <= right {
            if xy.x > xy.y {
                max = xy.x
            } else {
                max = xy.y
            }
            array.append(max+1)
        }
    }
    // let answer = array[Int(left)...Int(right)].map { $0 }
    // let answer = array[Int(left)...Int(right)] // Cannot convert return expression of type 'Array<Int>.SubSequence' (aka 'ArraySlice<Int>') to return type '[Int]'
    return array
}

/*
 func solution2(_ n:Int, _ left:Int64, _ right:Int64) -> [Int] {
     //      0       1         2         3       4         5        6        7       8
     // 1: [0,0] 2: [0,1]  3: [0,2] 2: [1,0] 2: [1,1] 3: [1,2] 3: [2,0] 3: [2,1] 3: [2,2]
     //                        3         2       2       3
     
     var array = [Int]()
     
     for idx in 0 ..< n*n {
         
         var xy = (x: 0, y: 0)
         xy.x = idx / n
         xy.y = idx % n
         
         // let max = max(xy.x, xy.y)
         var max = 0
         
         if idx >= left && idx <= right {
             if xy.x > xy.y {
                 max = xy.x
             } else {
                 max = xy.y
             }
             array.append(max+1)
         }
     }
     // let answer = array[Int(left)...Int(right)].map { $0 }
     // let answer = array[Int(left)...Int(right)] // Cannot convert return expression of type 'Array<Int>.SubSequence' (aka 'ArraySlice<Int>') to return type '[Int]'
     return array
 }
 */


print(solution(3, 2, 5))
print(solution(4, 7, 14))
/*
테스트 1 〉    통과 (11.56ms, 33.2MB)
테스트 2 〉    실패 (시간 초과)
테스트 3 〉    실패 (시간 초과)
테스트 4 〉    통과 (0.74ms, 16.4MB)
테스트 5 〉    통과 (0.38ms, 16.3MB)
테스트 6 〉    통과 (50.09ms, 34.2MB)
테스트 7 〉    통과 (56.98ms, 35.4MB)
테스트 8 〉    통과 (46.11ms, 33.9MB)
테스트 9 〉    통과 (4400.36ms, 1.02GB)
테스트 10 〉    통과 (4644.30ms, 1.02GB)
테스트 11 〉    통과 (3468.89ms, 1.02GB)
테스트 12 〉    실패 (시간 초과)
테스트 13 〉    실패 (시간 초과)
테스트 14 〉    실패 (시간 초과)
테스트 15 〉    실패 (시간 초과)
테스트 16 〉    실패 (시간 초과)
테스트 17 〉    실패 (시간 초과)
테스트 18 〉    실패 (시간 초과)
테스트 19 〉    실패 (시간 초과)
테스트 20 〉    실패 (시간 초과)
*/
