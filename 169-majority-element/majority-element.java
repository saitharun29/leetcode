class Solution {
    public int majorityElement(int[] nums) {
        int n=nums.length-1;
        Arrays.sort(nums);
        return nums[n/2];
    }
}