package Baekjoon.B8958;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // 문제를 맞은 경우 문제의 점수는 그 문제까지 연속된 O 의개수
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < N; i++) {
            String strs = sc.nextLine();
            int maxScore = 0;
            int L = strs.length();
            int cnt = 1;
            for (int j = 0; j < L; j++) {
                if (strs.charAt(j) == 'O') {
                    maxScore += cnt * 1;
                    cnt++;
                } else {
                    cnt = 1;
                }
            }
            System.out.println(maxScore);
        }
    }
}
