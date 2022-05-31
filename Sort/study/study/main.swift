//
//  main.swift
//  study
//
//  Created by JAEHYEON on 2022/05/25.
//

import Foundation

let sampleArray = [4, 7, 9, 2, 3, 5, 6, 1, 8]

class QuickSort {
    static func quickSort(_ arr : inout [Int]) {
        QuickSort.quickSort(&arr,0, arr.count - 1);
    }
    
    static func quickSort(_ arr : inout [Int], _ start : Int, _ end : Int) {
        let part2: Int = QuickSort.partition(&arr, start, end);
        if (start < part2 - 1) {
            QuickSort.quickSort(&arr, start, part2 - 1);
        }
        if (part2 < end) {
            QuickSort.quickSort(&arr, part2, end);
        }
    }
    
    static func partition(_ arr : inout [Int], _ start : Int, _ end : Int) -> Int {
        let pivot: Int = arr[(start + end) / 2]
        var start = start
        var end = end
        while (start <= end) {
            
            while (arr[start] < pivot) { start += 1 }
            while (arr[end] < pivot) { end -= 1 }
            
            if (start <= end) {
                QuickSort.swap(&arr, start, end);
                start += 1
                end -= 1
            }
        }
        return start;
    }
    
    static func swap(_ arr : inout [Int], _ start : Int, _ end : Int) {
        let tmp : Int = arr[start];
        arr[start] = arr[end];
        arr[end] = tmp;
    }
    
    static func printArray(_ arr : inout [Int]) {
        for data in arr{
            print(String(data) + ", ",terminator: "");
        }
        print();
    }
}
