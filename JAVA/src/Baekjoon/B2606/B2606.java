package Baekjoon.B2606;


import java.util.*;

public class B2606 {

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

//        System.out.println(adjList);

        int startNum = 1;
        int[] visited = new int[N + 1];
        int cnt = 0;
        // 1. 시작 컴퓨터 1 번

        // 2. Q 만들기
        // - adjList 의 1번째 인덱스의 리스트가 담긴 큐

        // 3. Q 를 돌면서 Q 가 비어있지 않으면 계속 돌기

        // 4. Q 를 돌면서 adjList 에 해당 인덱스가 가르키는 배열에서 반복하면서 방문처리

        // 5. Q 가 끝나면 방문 처리 되어있지 않은 인덱스 숫자 를 구하고 - 1 -> 0 번 인덱스 포함했기 때문에

        visited[1] = 1;
        Queue<Integer> Q = new LinkedList();
//        System.out.println(adjList.get(startNum));
        Q.add(startNum);

        while (!Q.isEmpty()) {
            int w = Q.poll();
//            System.out.println(w);
            for (int node : adjList.get(w)) {
                if (visited[node] == 0) {
                    visited[node] = 1;
                    Q.add(node);
                    cnt++;
                }
            }
        }

//        System.out.println(Arrays.toString(visited));
        System.out.println(cnt);
    }
}
