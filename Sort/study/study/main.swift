//
//  main.swift
//  study
//
//  Created by JAEHYEON on 2022/05/25.
//

import Foundation

let sampleArray = [4, 7, 9, 2, 3, 5, 6, 1, 8]

func quickSort(array: [Int]) -> [Int] {
    print(array)
    if array.count < 2 {
        return array
    } else {
        let P = array[0]
        let smaller = array.filter { $0 < P }
        let bigger = array.filter { $0 > P}
        return quickSort(array: smaller) + [P] + quickSort(array: bigger)
    }
}

print(quickSort(array: sampleArray))

// func quickSort(with array: Array<Int>) {
//
//     var N = array
//     print("N : \(N)")
//
//     let PL = 0
//     let P = N[PL]
//
//     var L = PL + 1
//     var R = N.count - L
//     // print("PL, P : \(PL), \(P)")
//     // print("L, R : \(L), \(R)")
//     print("N[L]: \(N[L]), N[R] : \(N[R])")
//     for _ in 0...2 {
//         if N[L] > P && N[R] < P {
//             print("yes")
//             let temp = N[L]
//             N[L] = N[R]
//             N[R] = temp
//         } else if N[L] > P && N[R] > P {
//             R -= 1
//         } else if N[L] < P && N[R] < P {
//             L += 1
//         }
//         print(array)
//     }
//
//
// }
