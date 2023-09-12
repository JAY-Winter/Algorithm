import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Rich {
    static boolean[] uniquePos;
    static int R, C, Q, answer;
    static int[][] board, update;
    static int[] maxRow, maxPosByRow;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc < T+1; tc++) {
            String[] input = br.readLine().split(" ");
            R = Integer.parseInt(input[0]);
            C = Integer.parseInt(input[1]);
            Q = Integer.parseInt(input[2]);

            // board 초기화
            board = new int[R][C];
            for (int r = 0; r < R; r++) {
                String[] line = br.readLine().split(" ");
                for (int c = 0; c < C; c++) {
                    board[r][c] = Integer.parseInt(line[c]);
                }
            }

            // 업데이트 되는 정보 초기화
            update = new int[Q][3];
            for (int q = 0; q < Q; q++) {
                String[] input2 = br.readLine().split(" ");
                int UR = Integer.parseInt(input2[0]);
                int UC = Integer.parseInt(input2[1]);
                int X = Integer.parseInt(input2[2]);
                update[q] = new int[]{UR, UC, X};
            }

            // 정답 구하기
            answer = 0;

            // 가로 맥스값 초기화
            maxRow = new int[R];
            maxPosByRow = new int[R];

            uniquePos = new boolean[C];
            // 행 별 최초 맥스값 위치 찾기
            initMaxRow();

            // 셀 업데이트 & Max 값 비교
            for (int q = 0; q < Q; q++) {
                updateCell(q);
//                System.out.println("maxPosByRow = " + Arrays.toString(maxPosByRow));
//                System.out.println("uniquePos = " + Arrays.toString(uniquePos));

            }
            System.out.println("#" + tc + " " + answer);
        }
    }

    private static void initMaxRow() {
        for (int r = 0; r < R; r++) {
            int tempMax = 0;
            int maxC = 0;
            for (int c = 0; c < C; c++) {
                if (board[r][c] > tempMax) {
                    tempMax = board[r][c];
                    maxC = c;
                }
            }
            maxPosByRow[r] = maxC;
            uniquePos[maxC] = true;
        }
    }

    private static void compareMax(int r, int c, int newVal) {
        int maxCol = maxPosByRow[r];
        if (newVal > board[r][maxCol]) {
            maxPosByRow[r] = c;
        }
    }

    private static void updateCell(int n) {
        int[] updateInfo = update[n];
        updateInfo[0] -= 1;
        updateInfo[1] -= 1;
        int r = updateInfo[0];
        int c = updateInfo[1];
        int x = updateInfo[2];
        board[r][c] = x;

        compareMax(r, c, x);
    }
}
