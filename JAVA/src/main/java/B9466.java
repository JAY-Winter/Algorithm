/*

    프로젝트 팀원 수에는 제한이 없다
    모든 학생들이 동일한 팀의 인원인 경우 같이 한 팀만 있을 수도 있다
    프로젝트를 함께하고 싶은 학생을 선택해야한다.(단 한 명만 선택할 수 있음)
    혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다


 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class B9466 {
    static ArrayList<int[][]> adj;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] students = new int[n];
            String line = br.readLine();
            for (int j = 0; j < line.length(); j++) {
                students[j] = Integer.parseInt(String.valueOf(line.charAt(j) - '0'));
            }
            System.out.println("students = " + Arrays.toString(students));

            adj = new ArrayList<>();
        }
    }
}
