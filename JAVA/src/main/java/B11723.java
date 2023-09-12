import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B11723 {
    static int s;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        s = 0;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            String command = input[0];

            switch (command) {
                case "add":
                    add(Integer.parseInt(input[1]));
                    break;
                case "remove":
                    remove(Integer.parseInt(input[1]));
                    break;
                case "check":
                    sb.append(check(Integer.parseInt(input[1]))).append("\n");
                    break;
                case "toggle":
                    toggle(Integer.parseInt(input[1]));
                    break;
                case "all":
                    all();
                    break;
                case "empty":
                    empty();
                    break;
            }
        }

        System.out.println(sb.toString());
    }

    public static void add(int x) {
        s |= (1 << x);
    }

    public static void remove(int x) {
        s &= ~(1 << x);
    }

    public static int check(int x) {
        return (s & (1 << x)) != 0 ? 1 : 0;
    }

    public static void toggle(int x) {
        s ^= (1 << x);
    }

    public static void all() {
        s = (1 << 21) - 1;
    }

    public static void empty() {
        s = 0;
    }
}
