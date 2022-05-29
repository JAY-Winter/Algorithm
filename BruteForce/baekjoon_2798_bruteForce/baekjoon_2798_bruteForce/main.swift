//
//  main.swift
//  baekjoon_2798_bruteForce
//
//  Created by JAEHYEON on 2022/05/29.
//

import Foundation


let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]
var sum: Int = 0 // 위치들의 합
var maxSum: Int = 0
let list = readLine()!.split(separator: " ").map { Int($0)! }

func blackJack() {
    for i in 0..<list.count {
        for j in i+1 ..< list.count {
            for k in j+1 ..< list.count {
                sum = list[i] + list[j] + list[k]
                if sum <= M && maxSum < sum {
                    maxSum = sum
                }
            }
        }
    }
    print(maxSum)
}

blackJack()


func isCountThree(N: Int) -> Bool {
    return N == 3 ? false : true
}



// 5,6,7,8,9 중 3개 고르고 21에 가까울, 예시일 때
// 5,6,7 > 5,6,8 해서 (21 - 합) 이 더 작은게 answer 에 들어간다.


// while isCountThree(N: count) {
//     print(list[C])
//     sum += list[C]
//     C += 1
//     count += 1
// }
//
// sumArr.append(sum)
// print(sumArr)
//
//
//
//
// C += 1
// count = 1
// }
