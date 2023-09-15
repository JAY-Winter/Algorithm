import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B24445 {
    static int N, M , R;
    static List<List<Integer>> graph = new ArrayList<>();


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        input(br);
        int[] answer = bfs();
        for (int i = 1; i < answer.length; i++) {

            System.out.println(answer[i]);

        }
    }

    public static void input(BufferedReader br) throws IOException {
        String[] line = br.readLine().split(" ");
        N = Integer.parseInt(line[0]);
        M = Integer.parseInt(line[1]);
        R = Integer.parseInt(line[2]);

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            String[] line2 = br.readLine().split(" ");
            int u = Integer.parseInt(line2[0]);
            int v = Integer.parseInt(line2[1]);
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
    }


    public static int[] bfs() {
        int[] visited = new int[N+1];
        visited[R] = 1;
        int seq = 1;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(R);
        System.out.println("graph = " + graph);
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            graph.get(cur).sort(Comparator.reverseOrder());
            for (Integer adj : graph.get(cur)) {
                if (visited[adj] == 0) {
                    seq++;
                    visited[adj] = seq;
                    queue.add(adj);
                }
            }
        }
        System.out.println("visited = " + Arrays.toString(visited));
        return visited;
    }


}
