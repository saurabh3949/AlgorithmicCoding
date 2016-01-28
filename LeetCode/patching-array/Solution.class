public class Solution {
    public int minPatches(int[] nums, int n) {
        long maxSum = 0;
        int count = 0;
        for(int i = 0; maxSum < n;){
            if (i >= nums.length || maxSum < nums[i] - 1){
                maxSum = 2*maxSum +1;
                count += 1;
            }
            else{
                maxSum += nums[i++];
            }
        }
        return count;
    }
}
