import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

/*
    치즈가 있는 칸 : 1
    치즈가 없는 칸 : 0
    가로, 세로 <= 100

    판의 가장자리에는 치즈가 없음
    치즈에는 하나 이상의 구멍이 있을 수 있다

    공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다

    공기와 접촉된 칸의 기준
    1. 부분 집합을 구한다
    2. 구한 부분 집합에서 끝 부분에 있는 애들이 녹는 애들


    Q : 치즈가 모두 녹아 없어지는데 걸리는 시간, 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여있는 칸의 개수
 */
public class B2636 {

    static int R;
    static int C;
    static int[][] board;
    static int[][] cheessRange;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        R = Integer.parseInt(input[0]);
        C = Integer.parseInt(input[1]);

        board = new int[R][C];
        cheessRange = new int[R][2];



        for (int i = 0; i < R; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < C; j++) {
                board[i][j] = Integer.parseInt(row[j]);
            }
        }


        searchCheeseRange();
        search();
    }
    private static void searchCheeseRange() {
        // 치즈의 범위를 먼저 찾기
        for (int r = 0; r < R; r++) {
            int[] line = board[r];
            cheessRange[r][0] = C+1;
            cheessRange[r][1] = -1;

            for (int c = 0; c < C; c++) {
                if (line[c] == 1) {
                    if (c < cheessRange[r][0]) {
                        cheessRange[r][0] = c;
                    } else if (c > cheessRange[r][1]) {
                        cheessRange[r][1] = c;
                    }
                }
            }
        }
        System.out.println("cheessRange = " + Arrays.deepToString(cheessRange));
    }

    private static void search() {
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        ArrayList<int[]> leakedCheeseList = new ArrayList<>();
        for (int r = 0; r < R; r++) {
            int[] line = board[r];
            for (int c = 0; c < C; c++) {
                // 공기일 때
                if (line[c] == 0 && (c >= cheessRange[r][0] || c <= cheessRange[r][1])) {
                    if (r == 3) {

                        System.out.println(r + " " +c);
                    }
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];
                        // 새로 바라보는 좌표가 범위 내 & 치즈일 때
                        if (nr < R && nr >= 0 && nc < C && nc >= 0 && board[nr][nc] == 1) {
                            int[] cheesePos = new int[]{nr, nc};
                                leakedCheeseList.add(cheesePos);
                        }
                    }
                }

            }
        }
        for (int[] cheese : leakedCheeseList) {
            int r = cheese[0];
            int c = cheese[1];

            board[r][c] = 0;
        }


        for (int[] b : board) {
            System.out.println("b = " + Arrays.toString(b));
        }
    }


}
