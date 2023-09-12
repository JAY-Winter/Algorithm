import java.util.Scanner;

public class RichDream {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tc = scanner.nextInt();

        for (int t = 1; t <= tc; t++) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int q = scanner.nextInt();

            int[][] grid = new int[n][m];
            int[] rowMax = new int[n];
            int[] colMax = new int[m];
            int totalSafeCells = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    grid[i][j] = scanner.nextInt();
                    rowMax[i] = Math.max(rowMax[i], grid[i][j]);
                    colMax[j] = Math.max(colMax[j], grid[i][j]);
                }
            }

            for (int i = 0; i < n; i++) {
                totalSafeCells += countMaxCells(grid[i], rowMax[i]);
            }

            for (int j = 0; j < m; j++) {
                totalSafeCells += countMaxCells(getColumn(grid, j), colMax[j]);
            }

            for (int i = 0; i < q; i++) {
                int r = scanner.nextInt() - 1;
                int c = scanner.nextInt() - 1;
                int x = scanner.nextInt();

                totalSafeCells -= countMaxCells(grid[r], rowMax[r]);
                totalSafeCells -= countMaxCells(getColumn(grid, c), colMax[c]);

                grid[r][c] = x;
                rowMax[r] = Math.max(rowMax[r], x);
                colMax[c] = Math.max(colMax[c], x);

                totalSafeCells += countMaxCells(grid[r], rowMax[r]);
                totalSafeCells += countMaxCells(getColumn(grid, c), colMax[c]);

            }
            System.out.println("#" + t + " " + totalSafeCells);
        }
    }

    private static int[] getColumn(int[][] grid, int col) {
        int n = grid.length;
        int[] column = new int[n];
        for (int i = 0; i < n; i++) {
            column[i] = grid[i][col];
        }
        return column;
    }

    private static int countMaxCells(int[] values, int maxValue) {
        int count = 0;
        for (int value : values) {
            if (value == maxValue) {
                count++;
            }
        }
        return count;
    }
}
