import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B6087 {

    private static final int MAX = 100;
    private static int W, H;
    private static char[][] MAP = new char[MAX][MAX];
    private static int[][] visited = new int[MAX][MAX];
    private static int[] dx = {0, 0, 1, -1};
    private static int[] dy = {1, -1, 0, 0};
    private static Pair start, end;

    static class Pair {
        int first;
        int second;

        Pair(int a, int b) {
            first = a;
            second = b;
        }
    }

    private static void input(Scanner scanner) {
        int tmp = 0;
        W = scanner.nextInt();
        H = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < H; i++) {
            String line = scanner.nextLine();
            for (int j = 0; j < W; j++) {
                MAP[i][j] = line.charAt(j);
                if (MAP[i][j] == 'C') {
                    if (tmp == 0) {
                        start = new Pair(i, j);
                        tmp++;
                    } else {
                        end = new Pair(i, j);
                    }
                }
                visited[i][j] = 987654321;
            }
        }
    }

    static class Node {
        int x, y, dir, cnt;

        Node(int x, int y, int dir, int cnt) {
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.cnt = cnt;
        }
    }

    public static int BFS() {
        Queue<Node> Q = new LinkedList<>();
        for (int i = 0; i < 4; i++) {
            Q.add(new Node(start.first, start.second, i, 0));
            visited[start.first][start.second] = 0;
        }

        while (!Q.isEmpty()) {
            Node current = Q.poll();
            int x = current.x;
            int y = current.y;
            int Dir = current.dir;
            int Cnt = current.cnt;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                int nCnt = Cnt;

                if (nx < 0 || ny < 0 || nx >= H || ny >= W) continue;
                if (MAP[nx][ny] == '*') continue;
                if (Dir != i) nCnt = nCnt + 1;
                if (visited[nx][ny] >= nCnt) {
                    visited[nx][ny] = nCnt;
                    Q.add(new Node(nx, ny, i, nCnt));
                }
            }
        }
        return visited[end.first][end.second];
    }

    public static void solution() {
        int R = BFS();
        System.out.println(R);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        input(scanner);
        solution();
        scanner.close();
    }
}
