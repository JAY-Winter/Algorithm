import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class B15649 {

    static int N;
    static int M;
    static int[] numbers;
    static boolean[] isSelected;
    public static void main(String[] args) throws IOException {
        BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(buff.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        numbers = new int[M];
        isSelected = new boolean[N + 1];
        System.out.println("numbers = " + Arrays.toString(numbers));
        perm(0);
    }

    private static void perm(int n) {
        if (n == M) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < M; i++) {
                sb.append(numbers[i]).append(' ');
            }
            System.out.println(sb.toString().trim());
            return;
        }

        for (int i = 1; i < N+1; i++) {
            if (!isSelected[i]) {
                isSelected[i] = true;
                numbers[n] = i;
                perm(n+1);
                isSelected[i] = false;
            }

        }
    }

}
