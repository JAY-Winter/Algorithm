package Baekjoon.B2606_2;

import java.util.*;

public class Main {

    public static void main(String[] args) {

        // 1 번 컴퓨터르 통해 바이러스에 걸리게 되는 컴퓨터의 수 출력
        Scanner sc = new Scanner(System.in);

        // N : 컴퓨터의 수
        int N = sc.nextInt();

        // 연결되어 있는 컴퓨터의 쌍의 수
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

        int[] visitied = new int[N + 1];
        Queue<Integer> Q = new LinkedList<>();
        Q.add(1);
        int cnt = 0;
        while (!Q.isEmpty()) {
            int node = Q.poll();
            for (int newNode : adjList.get(node)) {
                if (visitied[newNode] == 0) {
                    visitied[newNode] = 1;
                    Q.add(newNode);
                    cnt++;
                }
            }
        }
        System.out.println(cnt - 1);
    }
}

