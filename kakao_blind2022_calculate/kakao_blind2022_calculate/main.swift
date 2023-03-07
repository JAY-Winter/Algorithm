//
//  main.swift
//  kakao_blind2022_calculate
//
//  Created by JAEHYEON on 2022/06/15.
//

import Foundation

func solution(_ fees:[Int], _ records:[String]) -> [Int] {
    var recordsByCar: [String: [Int]] = [:]
    
    // 매개변수 records 정리 구문
    for record in records {
        let splitedRecord = record.split(separator: " ")
        let carNumber = String(splitedRecord[1])
        let splitTime = splitedRecord[0]
            .split(separator: ":")
            .map { Int($0)! }
        
        let time = (hour: splitTime[0], min: splitTime[1])
        // records 는 IN&OUT 순으로 정렬되어있기 때문에 IN or OUT 상관없이 (시 + 분)으로 계산
        
        recordsByCar[carNumber, default: []].append(converseTime(with: time))
    }
    // IN 만 했을 때 (23:59) append
    appendTime(&recordsByCar)
    
    // [carNumber : [conversedTimeList]]
    for (car, timeList) in recordsByCar {
        var totalCost = 0
        var spendTime = 0



        // 5961 : [334, 479, in, out, in ...]

        // IN > OUT 순으로 추가되어있는 time 을 (OUT - IN) 하는 구문
        print("timeList : \(timeList)")
        for i in 0 ..< timeList.count {
            if i % 2 == 0 {
                spendTime -= timeList[i]
            } else {
                spendTime += timeList[i]
            }
        }

        // 정리된 spendTime 을 매개변수(기본시간)으로 구분
        if spendTime > fees[0] {
            // ceil 을 최대한 쓰지 말자.... Double 이 명확한 값을 지칭하는지 몰라서 ,, ,, > 정확도가 높다, 다만 정확한 건 아니다...
            totalCost = fees[1] + Int(ceil(Double(spendTime - fees[0]) / Double(fees[2]))) * fees[3]
        } else {
            totalCost = fees[1]
        }
        // totalCost >>
        // 차종별 딕셔너리 마지막 인데스에 추가
        recordsByCar[car, default: []].append(totalCost)
    }
    print("recordsByCarNumber : \(recordsByCar)")
    
    return getResult(&recordsByCar)
}

func converseTime(with time: (hour: Int, min: Int)) -> Int {
    return ((time.hour) * 60 ) + time.min
}

func appendTime(_ records: inout [String: [Int]]) {
    records
        .keys
        .forEach {
        if records[$0]!.count % 2 == 1 {
            records[$0]!.append(1439)
        }
    }
}

func getResult(_ records: inout [String: [Int]]) -> [Int] {
    var answer: [Int] = []
    // recordsByCar
    records
        .keys
        .sorted()
        .forEach {
        answer.append(records[$0]!.last!)
    }

    return answer
}




print(
    solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
)

