//
//  main.swift
//  programmers_2
//
//  Created by JAEHYEON on 2022/05/20.
//

import Foundation

func solution(_ clothes:[[String]]) -> Int {
    let clothesInfo = arrangeClothes(clothes)
    print(clothesInfo)
    
    var result: Int = 0
    let categoryCount: Int = clothesInfo.values.count
    
    if categoryCount >= 2{
        for cloth in clothesInfo.values {
            result += cloth.count
            result += 1
        }
    } else {
        for i in clothesInfo.values {
            result += i.count
        }
    }
    print("result: \(result)")

    return result
}

func arrangeClothes(_ clothes: [[String]]) -> [String: [String]] {
    var clothesInfo: [String: [String]] = [:]
    
    let category = clothes.map {$0[1] }
    let cloth = clothes.map {$0[0] }
    
    for (category, cloth) in zip(category, cloth) {
        
        if clothesInfo[category] != nil {
            clothesInfo[category]?.append(cloth)
        } else {
            clothesInfo[category] = [cloth]
        }
    }
    return clothesInfo
}

let case1 = solution([
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"]
    ])

let case2 = solution([
    ["crowmask", "face"],
    ["bluesunglasses", "face"],
    ["smoky_makeup", "face"]
    ])

let case3 = solution([
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
    ["red_jean", "pants"]
    ])
