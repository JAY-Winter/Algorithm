//
//  main.swift
//  hash_algorithm
//
//  Created by JAEHYEON on 2022/05/19.
//

import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {

    let splitedReport = report.map { $0.split(separator: " ") }
    var reportInfo: [String: Set<String>] = [:]
    var emailInfo: [String: Int] = [:]
    var result: [Int] = []

    for id in id_list {
        emailInfo[id] = 0
    }
    
    for user in splitedReport {
        if reportInfo[String(user[1])] != nil {
            reportInfo[String(user[1])]?.insert(String(user[0]))
        } else {
            reportInfo[String(user[1])] = [String(user[0])]
        }
    }

    for (_, value) in reportInfo {
        for user in value {
            if value.count >= k {
                emailInfo[user]! += 1
            }
        }
    }
    print(emailInfo)
    
    while true {
        for id in id_list {
            for (key, value) in emailInfo {
                if id == key {
                    result.append(value)
                }
            }
        }
        if result.count == id_list.count {
            break
        }
    }
    print(result)
    return result
}

let case1 = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
let case2 = solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
