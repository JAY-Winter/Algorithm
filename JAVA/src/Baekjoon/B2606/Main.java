package Baekjoon.B2606;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        List<List<Integer>> adjList = new ArrayList<>();

        for (int i = 0; i < N + 1; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }

        int cnt = 0;
        // 0. 시작 컴퓨터 1 번
        int startNum = 1;
        // 1. 방문 처리용 배열 생성
        int[] visited = new int[N + 1];
        visited[1] = 1;
        // 2. Q 만들기
        // - adjList 의 1번째 인덱스의 리스트가 담긴 큐
        Queue<Integer> Q = new LinkedList();
        Q.add(startNum);
        // 3. Q 를 돌면서 Q 가 비어있지 않으면 계속 돌기
        while (!Q.isEmpty()) {
        // 4. FIFO : adjList 에 해당 인덱스가 가르키는 배열에서 반복하면서 방문처리
            int w = Q.poll();
            for (int node : adjList.get(w)) {
                // 5. 해당 배열을 순회하면서 방문하지 않은 인덱스일 때 방문처리 후 cnt++
                if (visited[node] == 0) {
                    visited[node] = 1;
                    Q.add(node);
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }


}
