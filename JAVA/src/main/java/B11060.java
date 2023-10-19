import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B11060 {
    /*
    - 칸 별 Ai 이하만큼 오른쪽으로 떨어진 칸으로 한 번에 점프할 수 있다
    - 만약 3번째 칸에 쓰여있는 수가 3이면, 4, 5, 6 중 하나로 점프할 수 있다
    - 현재 미로의 가장 왼쪽 0 에 있고, 가장 오른쪽으로 가려고한다
    Q) 이때, 최소 몇 번 점프를 해야할 수 있을까?
    갈 수 없은 경우 -1 을 출력한다
     */
    static int N;
    static int[] board;
    static int[] count;
    static int INF = 987654321;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        sc.nextLine();
        String[] input = sc.nextLine().split(" ");
        board = new int[N];
        count = new int[N];
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(input[i]);
            board[i] = num;
            count[i] = 987654321;
        }
        count[0] = 0;
        int answer = bfs();
        System.out.println(answer);
    }
    public static int bfs() {
        Queue<int[]> Q = new LinkedList<>();
        Q.offer(new int[]{0, 0});

        while (!Q.isEmpty()) {
            int[] cur = Q.poll();
            int now = cur[0];
            int cnt = cur[1];

            if (now == N - 1) {
                return cnt;
            }

            for (int i = 1; i <= board[now]; i++) {
                if (now + i >= N) break;

                if (count[now + i] > cnt + 1) {
                    count[now + i] = cnt + 1;
                    Q.add(new int[]{now + i, cnt + 1});
                }
            }
        }
        return -1;
    }
}
