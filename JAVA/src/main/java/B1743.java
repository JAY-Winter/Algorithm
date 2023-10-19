import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B1743 {
    /*
    Q) 첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력하라
     */
    static int N, M, K;
    static char[][] board;
    static int answer = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        K = Integer.parseInt(input[2]);

        board = new char[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = '.';
            }
        }

        for (int i = 0; i < K; i++) {
            String[] input2 = sc.nextLine().split(" ");
            int r = Integer.parseInt(input2[0]);
            int c = Integer.parseInt(input2[1]);
            r -= 1;
            c -= 1;
            board[r][c] = '#';
        }
        bfs();
        System.out.println(answer);
    }

    public static void bfs() {
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        boolean[][] visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                // bfs 탐색 시작
                if (board[i][j] == '#') {
                    int tempResult = 1;
                    visited[i][j] = true;
                    Queue<Coordination> Q = new LinkedList<>();
                    Coordination coor = new Coordination(i, j);
                    Q.add(coor);
                    while (!Q.isEmpty()) {
                        int r, c;
                        Coordination cur_coor = Q.poll();
                        r = cur_coor.r;
                        c = cur_coor.c;

                        for (int d = 0; d < 4; d++) {
                            int nr = r + dr[d];
                            int nc = c + dc[d];

                            if (nr < N && nr >= 0 && nc < M && nc >= 0 && !visited[nr][nc] && board[nr][nc] == '#') {
                                tempResult++;
                                visited[nr][nc] = true;
                                Q.add(new Coordination(nr, nc));
                            }
                        }
                    }
                    answer = Math.max(answer, tempResult);
                }
            }
        }
    }

    public static class Coordination {
        int r, c;

        public Coordination(int r, int c) {
            this.r = r;
            this.c = c;
        }

    }

}
