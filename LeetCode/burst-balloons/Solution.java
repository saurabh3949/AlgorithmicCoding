public class Solution {
    public int maxCoins(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int n = nums.length;
        int[][] coins = new int[n + 1][n + 1]; // coins[i][j] is max coins by bursing in [i,j) range
        for (int j = 1; j <= n; j++) {
            for (int i = j - 1; i >= 0; i--) {
                int max = 0;
                for (int k = i; k <= j - 1; k++) {// k is index of last balloon bursted in [i,j)
                    max = Math.max(max, coins[i][k] + coins[k + 1][j] + nums[k] * (j == n ? 1 : nums[j]) * (i == 0 ? 1 : nums[i - 1]));
                } // [i+1,j) is computed before [i,j), which makes above formula possible
                coins[i][j] = max;
            }
        }
        return coins[0][n];
    }
}
