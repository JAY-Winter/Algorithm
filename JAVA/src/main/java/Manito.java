import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;


public class Manito {
    static ArrayList<ArrayList<Integer>> adj; // 짝수 : 연결 번호, 홀수 : 연결 값
    static int[] visited;
    static int answer;
    static int INF = 987654321;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();
        for (int tc = 1; tc < T+1; tc++) {
            String[] NM = sc.nextLine().split(" ");
            int N = Integer.parseInt(NM[0]);
            int M = Integer.parseInt(NM[1]);

            adj = new ArrayList<>(N+1);
            for (int i = 0; i < N+1; i++) {
                adj.add(new ArrayList<>());
            }

            for (int m = 0; m < M; m++) {
                String[] input = sc.nextLine().split(" ");
                int[] rel = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();
                int X = rel[0];
                int Y = rel[1];
                int Z = rel[2];

                adj.get(X).add(Y);
                adj.get(X).add(Z);
            }


            answer = INF;
            for (int num = 1; num < N + 1; num++) {
                visited = new int[N+1];
                visited[num] = 1;
                search(num, num, 0);
            }

            if (answer == INF) {
                answer = -1;
            }
            System.out.println("#" + tc + " " + answer);
        }
    }

    private static void search(int start, int current, int cost) {
        int L = adj.get(current).size();
        for (int i = 0; i < L; i += 2) {
            int next = adj.get(current).get(i);
            int nextCost = adj.get(current).get(i + 1);
            if (cost + nextCost >= answer) {
                continue;
            }
            if (next == start) {
                answer = Math.min(answer, cost + nextCost);
                continue;
            }
            if (visited[next] == 0 && cost + nextCost < answer) {
                visited[next] = 1;
                search(start, next, cost + nextCost);

            }
        }
    }
}
