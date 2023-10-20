import java.util.*;

public class B17141 {
/*
- 바이러스
    빈 칸은 바이러스를 놓을 수 있는 칸이다.
    상하좌우로 인접한 모든 빈칸으로 동시에 복제되며, 1초가 걸린다

- board
    0 : 빈 칸
    1 : 벽
    2 : 바이러스를 놓을 수 있는 칸

Q) 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력하라
    안 되는 경우에는 -1 을 출력한다

 */

    static int N, M;
    static int[][] board;
    static ArrayList<int[]> virusPosition;
    static boolean[] checked;
    static int[] dr = new int[]{-1, 1, 0, 0};
    static int[] dc = new int[]{0, 0, -1, 1};
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);

        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            String[] line = sc.nextLine().split(" ");
            for (int j = 0; j < N; j++) {
                int el = Integer.parseInt(line[j]);
                board[i][j] = el;
            }
        }

        // 바이러스 조합하기
        virusPosition = findVirusPosition();
        checked = new boolean[virusPosition.size()];
        setVirusAndSearch(0, 0, new ArrayList<>());

        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
    }

    public static ArrayList<int[]> findVirusPosition() {
        ArrayList<int[]> result = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 2) {
                    result.add(new int[]{i, j});
                }
            }
        }
        return result;
    }

    public static void setVirusAndSearch(int n, int prev, ArrayList<Integer> viruses) {
        if (n == M) {
            // search 시작
            int[][] tempBoard = deepCopy(board);
            int[][] time = new int[N][N];

            for (int[] row : time) Arrays.fill(row, -1);

            for (int i = 0; i < N; i++) {
                tempBoard[i] = board[i].clone();  // 깊은 복사
            }

            ArrayList<int[]> allViruses = new ArrayList<>();

            for (int virus : viruses) {
                int[] position = virusPosition.get(virus);
                int r = position[0];
                int c = position[1];
                time[r][c] = 0;

                allViruses.add(new int[]{r, c});
            }


            while (!allViruses.isEmpty()) {
                ArrayList<int[]> newViruses = new ArrayList<>();
                for (int[] viruse : allViruses) {
                    int r = viruse[0];
                    int c = viruse[1];

                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];

                        if (nr >= N || nr < 0 || nc >= N || nc < 0) continue;
                        if (time[nr][nc] >= 0) continue;
                        if (tempBoard[nr][nc] == 1) continue;

                        time[nr][nc] = time[r][c] + 1;
                        newViruses.add(new int[]{nr, nc});
                    }
                }
                allViruses = newViruses;
            }

            int tempAnswer = checkSpread(tempBoard, time);
            if (tempAnswer != -1) {
                answer = Math.min(answer, tempAnswer);
            }
            return;
        }

        for (int i = prev; i < virusPosition.size(); i++) {
            if (!checked[i]) {
                checked[i] = true;
                ArrayList<Integer> tempViruses = (ArrayList<Integer>) viruses.clone();
                tempViruses.add(i);
                setVirusAndSearch(n + 1, i, tempViruses);
                checked[i] = false;
            }
        }
    }

    private static int[][] deepCopy(int[][] board) {
        int[][] copy = new int[board.length][];
        for (int i = 0; i < board.length; i++) {
            copy[i] = board[i].clone();
        }
        return copy;
    }

    public static int checkSpread(int[][] board, int[][] time) {
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if ((board[i][j] == 0 || board[i][j] == 2) && time[i][j] == -1) {
                    return -1;
                }
                result = Math.max(result, time[i][j]);
            }
        }
        return result;
    }
}
