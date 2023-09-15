import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B14940 {

    static int N;
    static int M;
    static int[][] arr;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] NM = sc.nextLine().split(" ");

        N = Integer.parseInt(NM[0]);
        M = Integer.parseInt(NM[1]);

        arr = new int[N][M];

        for (int i = 0; i < N; i++) {
            String[] line = sc.nextLine().split(" ");
            for (int j = 0; j < M; j++) {
                int el = Integer.parseInt(line[j]);
                arr[i][j] = el;
            }
        }

        int[][] answer = bfs();


        for (int[] line : answer) {
            for (int el : line) {
                System.out.print(el + " ");
            }
            System.out.println();
        }
    }


    public static int[][] bfs() {
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        int[][] res = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 0) {
                    res[i][j] = 0;
                } else {
                    res[i][j] = -1;
                }
            }
        }

        // 시작지점 초기화
        int[][] visited = new int[N][M];
        int[] targetPoint = findTargetPoint();
        int initR = targetPoint[0];
        int initC = targetPoint[1];
        visited[initR][initC] = 1;
        res[initR][initC] = 0;

        // Queue
        Queue<int[]> queue = new LinkedList<>();
        queue.add(targetPoint);
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int r = now[0];
            int c = now[1];

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr >= N || nr < 0 || nc >= M || nc < 0) {
                    continue;
                }

                if (arr[nr][nc] == 0) {
                    continue;
                }

                if (visited[nr][nc] == 1) {
                    continue;
                }

                visited[nr][nc] = 1;
                res[nr][nc] = res[r][c] + 1;
                queue.add(new int[]{nr, nc});
            }
        }
        return res;
    }

    public static int[] findTargetPoint() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 2) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }
}
