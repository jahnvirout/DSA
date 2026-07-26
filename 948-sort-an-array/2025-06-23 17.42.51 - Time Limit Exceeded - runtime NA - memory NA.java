class Solution {
    public int[] sortArray(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n-1; i++) {
            int smallestidx = i;
            for (int j = i+1; j < n; j++) {
                if (nums[smallestidx]>nums[j]) {
                    smallestidx = j;
                }
                
            }
        
        int a = nums[i];
        nums[i] = nums[smallestidx];
        nums[smallestidx] = a;
        
    }
    return nums;
}
}
