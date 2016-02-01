public class Solution {
    public int findDuplicate(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        for (int i: nums){
            int no = nums[Math.abs(i)];
            if (no < 0) return Math.abs(i);
            else {
                nums[Math.abs(i)] *= -1;
            }
        
        }
        return 0;
    }
}
