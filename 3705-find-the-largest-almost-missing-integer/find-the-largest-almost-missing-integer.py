class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        rep = Counter(nums)
        if k==1:
            return max([x for x in nums if rep[x]==1], default= -1)
        ans= -1
        if rep[nums[0]] == 1:
            ans= max(ans,nums[0])
        if rep[nums[-1]]== 1:
            ans= max(ans,nums[-1])
        return ans