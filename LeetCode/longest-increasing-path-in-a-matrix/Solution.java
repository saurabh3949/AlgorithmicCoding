/**
 * Created by saurabh on 30/01/16.
 */
public class Solution {
    int[] dx = {0, 0, -1, 1};
    int[] dy = {1, -1, 0, 0};
    int m;
    int n;
    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        m = matrix.length;
        n = matrix[0].length;

        int answer = 0;
        int[][] sol = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                answer = Math.max(answer, dfs(sol, matrix, i, j));
            }
        }
        return answer;
    }

    private int dfs(int sol[][], int matrix[][], int i, int j){
        if (sol[i][j] != 0){
            return sol[i][j];
        }
        boolean hasNeighbours = false;
        for (int dir = 0; dir < 4; dir++) {
            int y = i + dy[dir];
            int x = j + dx[dir];

            if (x >= 0 && x < n && y >= 0 && y < m && matrix[y][x] > matrix[i][j]){
                sol[i][j] = Math.max(sol[i][j], 1 + dfs(sol, matrix, y, x));
                hasNeighbours = true;
            }

        }
        if (hasNeighbours == false){
            sol[i][j]++;
        }
        return sol[i][j];
        
    }
}

