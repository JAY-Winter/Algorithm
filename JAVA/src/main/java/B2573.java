import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/*
    빙산의 높이는 배열의 각 칸에 양의 정수로 저장
    바다 : 0

    빙산은 바닷물에 많이 접해있는 부분에서 더 빨리 줄어듬
    배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이
    저장된 칸의 개수만큼 줄어든다
    단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다
    바닷물은 호수처럼 빙산에 둘러싸여있을 수도 있다

    Q: 한 더엉리의 빙산이 주어질 때, 두덩어리 이상으로 분리되는 최초의 시간을 구하라
    만약, 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0 을 출력

 */
public class B2573 {
    static int R;
    static int C;
    static int[][] board;
    static int answer;
    static int[] dr;
    static int[] dc;
    static int[][] count;
    static int[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        R = Integer.parseInt(input[0]);
        C = Integer.parseInt(input[1]);
        dr = new int[]{-1, 1, 0, 0};
        dc = new int[]{0, 0, -1, 1};
        board = new int[R][C];

        for (int i = 0; i < R; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < C; j++) {
                int el = Integer.parseInt(line[j]);
                board[i][j] = el;
            }
        }
        search();

        System.out.println(answer);
    }
    private static void search() {
        answer = 0;
        while (true) {
            int group = 0;
            int icebergCnt = 0;
            visited = new int[R][C];
            count = new int[R][C];

            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    if (board[r][c] != 0 && visited[r][c] == 0) {
                        answer ++;
                        group ++;
                        icebergCnt ++;
                        // 그룹이 두 개 이상일 때
                        if (group == 2) {
                            return;
                        // 그룹이 두 개 이상이 아닐 때 탐색
                        } else {
                             bfs(r, c);
                        }
                    }
                }
            }
            // 탐색했는데도 불구하고 빙하가 없을 때
            if (icebergCnt == 0) {
                answer = 0;
                return;
            // 빙하가 있을 때 녹여야함
            } else {
                melting();
            }
        }
    }
    private static void bfs(int startR, int startC) {
        Queue<int[]> queue = new LinkedList<>();

        queue.add(new int[]{startR, startC});

        while (!queue.isEmpty()) {
            int[] el = queue.poll();
            int r = el[0];
            int c = el[1];
            visited[r][c] = 1;
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr < R && nr >= 0 && nc < C && nc >= 0 && visited[nr][nc] == 0) {
                    // 근접 좌표가 빙하일 때
                    if (board[nr][nc] != 0) {
                        queue.add(new int[]{nr, nc});
                        visited[nr][nc] = 1;
                    // 근접 좌표가 호수일 때
                    } else {
                        count[r][c] ++;
                    }
                }
            }
        }
    }

    private static void melting() {
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                int cnt = count[r][c];
                board[r][c] =- cnt;
                if (board[r][c] < 0) {
                    board[r][c] = 0;
                }

            }
        }


    }
}


/*















 */