import Foundation

struct heap {
    var lastn = 0
    var heap : [Int] = []
    
    init(_ size: Int) {
        lastn = 0
        heap = [Int](repeating: 0, count: size)
    }
    
    mutating func push(_ input: Int, comp: (_ s1: Int,_ s2: Int) -> Bool) {
        lastn += 1
        heap[lastn] = input
        var C = lastn, P = C / 2
        
        while P > 0 && !comp(heap[P], heap[C]) {
            heap.swapAt(P, C)
            C = P; P = C / 2
        }
    }
    
    mutating func pop(comp: (_ s1: Int,_ s2: Int) -> Bool) {
        heap[1] = heap[lastn]
        
        lastn -= 1
        
        var P = 1, L = 2, R = 3, C = 0
    
        while L <= lastn {
            if R > lastn {
                C = L
            }else { // 일반적인상황
                C = comp(heap[L], heap[R]) ? L: R
            }
            if comp(heap[P], heap[C]) {
                break
            }
            heap.swapAt(P, C)
            
            P = C;
            L = P * 2;
            R = L + 1
        }
    }
    
    func top() -> Int {
        return heap[1]
    }
    
    func isEmpty() -> Bool {
        return lastn == 0
    }
}

let compmax = { (_ s1: Int, _ s2: Int) -> Bool in
    return s1 >= s2
}

let compmin = {(_ s1: Int, _ s2: Int)->Bool in
    return s1 <= s2
}

let N = Int(readLine()!)!
var hq: heap = heap(100001)

for _ in 0..<N {
    let x = Int(readLine()!)!
    if x == 0 {
        if hq.isEmpty() {
            print(0)
        } else {
            print(hq.heap[1])
            hq.pop(comp: compmin)
        }
    } else {
        hq.push(x, comp: compmin)
    }
}
