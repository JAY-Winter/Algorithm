package Baekjoon.B2178;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    static Scanner sc = new Scanner(System.in);
    static int N = sc.nextInt();
    static int M = sc.nextInt();
    static int[][] maze = new int[N][M];

    public static void main(String[] args) {
        // init maze
        for (int i = 0; i < N; i++) {
            String row = sc.next();
            for (int j = 0; j < M; j++) {
                maze[i][j] = row.charAt(j) - '0';
            }
        }

        int result = bfs();
        System.out.println(result);
    }

    public static int bfs() {
        // 1. (0, 0) 시작
        int r = 0;
        int c = 0;
        Queue<int[]> Q = new LinkedList<>();
        Q.add(new int[]{r, c});
        // 2. Q 가 비어있지 않으면 진행
        while (!Q.isEmpty()) {
            // 2-1. (N, M) 에 도착하지 않았을 때
            // 3. 상 하 좌 우를 살피며 이동
            int[] pos = Q.poll();
            int a = pos[0];
            int b = pos[1];

            int[] dr = {-1, 1, 0, 0};
            int[] dc = {0, 0, -1, 1};
            for (int d = 0; d < 4; d++) {
                int new_r = a + dr[d];
                int new_c = b + dc[d];
                // 3-1. 이동해야할 위치 값이 배열 값보다 크거나 또는 0 보다 작으면 패스
                if (new_r >= N || new_c >= M || new_r < 0 || new_c < 0) {
                    continue;
                }
                // 3-2. 이동해야할 위치 값이 0 이면 패스
                if (maze[new_r][new_c] == 0) {
                    continue;
                }
                // 3-3. 이동해야할 위치가 1 이면 이동하는 좌표의 값을 현재 위치 값 + 1
                if (maze[new_r][new_c] == 1) {
                    maze[new_r][new_c] = maze[a][b] + 1;
                    int[] new_pos = {new_r, new_c};
                    Q.add(new_pos);
                }
            }
        }
        return maze[N - 1][M - 1];
    }
}
