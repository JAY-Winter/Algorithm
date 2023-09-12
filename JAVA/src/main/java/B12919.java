/*

    두 문자열 S, T 가 주어졌을 때, S 를 T 로 바꾸는 게임

    1. 문자열의 뒤에 A 를 추가한다
    2. 문자열의 뒤에 B 를 추가하고 문자열을 뒤집는다

    Q : 주어진 조건을 이용해서 S 를 T 로 만들 수 있는지 없는지 알아내라

    2 <= T <= 50, S < T
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B12919 {
    static String S;
    static StringBuilder T;
    static int L;
    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine();
        T = new StringBuilder(br.readLine());
        L = T.length();

        StringBuilder str = new StringBuilder();
        answer = 0;
        search(0, str);
        System.out.println(answer);
    }

    private static void search(int n, StringBuilder str) {
        if (n == L) {
            if (str.toString().equals(T.toString())) {
                answer = 1;
            }
            return;
        }

        // A 추가
        StringBuilder newStrA = new StringBuilder(str);
        newStrA.append('A');
        search(n + 1, newStrA);

        // B 추가 & Reverse
        StringBuilder newStrB = new StringBuilder(str);
        newStrB.append('B').reverse();
        search(n + 1, newStrB);

    }

}
