import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class B25757 {

    static int playersCnt;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split(" ");
        int N = Integer.parseInt(line[0]);
        String type = line[1];

        playersCnt = countPlayer(type);

        /*
        1. 카운트할 플레이인원수 구함
        2. 사람별로 중복 인원제거하고 카운트 1씩 할당 -> 맵
        3. 해당 맵을 순회하면서 플레이인원수 만큼 카운트하고 카운팅된 사람은 값을 0으로
        4. 다 순회했음에도 불구하고 플레이인원수 만큼 카운트 안되면 끗
         */

        // 플레이어 세팅
        Map<String, Integer> players = new HashMap<String, Integer>();

        while (N-- > 0) {
            String playerName = sc.nextLine();
            players.put(playerName, 1);
        }
        int answer = game(players);
        System.out.println(answer);
    }

    public static int countPlayer(String type) {
        switch (type) {
            case "Y":
                return 2;
            case "F":
                return 3;
            case "O":
                return 4;
            default:
                return 0;
        }
    }

    public static int game(Map<String, Integer> players) {
        int tempPlayersCnt = 0;
        int playingCnt = 0;

        for (Map.Entry<String, Integer> entry : players.entrySet()) {

            String name = entry.getKey();
            Integer number = entry.getValue();

            if (number != 0) {
                players.put(name, 0);
                tempPlayersCnt++;
            }
            if (tempPlayersCnt == playersCnt - 1) {
                playingCnt++;
                tempPlayersCnt = 0;
            }
        }
        return playingCnt;
    }
}
