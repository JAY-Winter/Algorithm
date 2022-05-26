//
//  main.swift
//  baekjoon_1927_heap
//
//  Created by JAEHYEON on 2022/05/23.
//

import Foundation

// 힙이란 데이터에서 최소 또는 최대 값을 빠르게 찾기 위한 이진트리구조...
struct Heap<T: Comparable> { // 비교가 가능한 데이터면 모두 담게 Comparable 프로토콜을 채택
    var heap: Array<T> = []
    
    init() { }
    
    init(data: T) {
        heap.append(data) // 0번 index 채우기
        heap.append(data) // 실제 Root Node 채우기 > 실제 Node 시작은 1번 index 부터 시작
    }
    
    mutating func insert(_ data: T) {
        if heap.isEmpty { // heap 이 공란일 때
            heap.append(data)
            heap.append(data) // data 를 2번 넣어주는 이유는, 실제 Node 시작은 1번 index 부터 시작하기 때문
            return
        }
        // heap 이 차있을 때
        heap.append(data)
        
        // insertIndex 가 부모노드에 따라서 움직여야하는지 구분하는 메서드
        func isMoveUp(_ insertIndex: Int) -> Bool {
            if insertIndex <= 1 { // index 가 1 보다 작거나 같으면 어쩄든 RootNode 로 되는 것이니 움직이지 않아도됨
                return false
            }
            let parentIndex: Int = insertIndex / 2 // 부모노드는 자식 노드의 1/2 이다. 즉, 완전이진트리 경우 자식 노드는 부모 노드(N)의 (Left, Right) = (2N, 2N + 1)
            return heap[insertIndex] > heap[parentIndex] ? true : false // 삽입한 노드, 즉 자식 노드가 부모 노드보다 클 경우에는 isMoveUp 에 true 가 반환되면서 움직임 그 반대일 경우 false 
        }
        // insertIndex 의 위치는 heap Array 의 마지막 순서
        var insertIndex: Int = heap.count - 1
        
        // insertIndex 즉, 추가한 노드(자식 노드)가 움직이는 경우(true)에 해당 시, while 문 반복
        while isMoveUp(insertIndex) {
            let parentIndex: Int = insertIndex / 2 // 부모 노드는 동일하게 자식 노드의 1/2 다
            heap.swapAt(insertIndex, parentIndex) // array 의 기본 메서드 swapAt() 을 사용하여 자식 노드와 부모 노드의 위치를 바꿔줌, 여기서 swapAt($0, $1) 의 의미는 index 위치를 말함
            insertIndex = parentIndex // 위 heap.swapAt() 을 통해서 heap 배열의 인덱스 위치가 바뀜, 근데 여기서 insertIndex = parentIndex 해준 이유는 바뀌어진 부모노드 값이 또 움직이는 경우가 있는지 확인하기 위해서 이와 같이 값 교환을 통해 반복문이 작동하게 된다
        }
        print(heap)
    }
}


var heap = Heap.init(data: 0)
heap.insert(32)
heap.insert(53)
heap.insert(61)
heap.insert(1)
heap.insert(2)
heap.insert(100)
heap.insert(42)
heap.insert(58)
heap.insert(98)
heap.insert(72)


let test1 = 5

