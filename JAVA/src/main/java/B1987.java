import java.util.Scanner;


public class B1987 {
    /*
        말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데,
        새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온
        모든 칸에 적혀 있는 알파벳과는 달라야 한다.
        즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다
        좌측 상단에서 시작해서, 말이 최대한 몇칸을 지날 수 있는지 구하라
        말이 지나는 칸은 좌측 상단의 칸도 포함된다


    */
    static int R;
    static int C;
    static char[][] board;
    static boolean[] isVisited;
    static int[] dr;
    static int[] dc;
    static int answer;


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();
        board = new char[R][C];
        isVisited = new boolean[26];
        for (int i = 0; i < R; i++) {
            String row = sc.next();
            for (int j = 0; j < C; j++) {
                board[i][j] = row.charAt(j);
            }
        }

        dr = new int[]{-1, 1, 0, 0};
        dc = new int[]{0, 0, -1, 1};

        answer = 0;




        dfs(0, 0, 0);
        System.out.println(answer);
    }


    public static void dfs(int r, int c, int cnt) {
        int idx = board[r][c] - 65;
        if (isVisited[idx]) {
            answer = Math.max(answer, cnt);
            return;
        }

        isVisited[idx] = true;

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < R && nr >= 0 && nc < C && nc >= 0) {
                dfs(nr, nc, cnt + 1);
            }
        }

        isVisited[idx] = false;


    }
}
