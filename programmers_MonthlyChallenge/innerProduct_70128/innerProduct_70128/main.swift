import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var result = 0
    var arr = [Int]()
    
    for i in 0 ..< a.count {
        for j in 0 ..< b.count {
            if i == j {
                let c = a[i] * b[j]
                arr.append(c)
            }
        }
    }
    result = arr.reduce(0) { $0 + $1 }
    
    return result
}

func solution2(_ a:[Int], _ b:[Int]) -> Int {
    var result2 = 0
    
    for (i, j) in zip(a, b) {
        result2 += i * j
    }
    
    return result2
}
