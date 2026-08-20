class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a=[nums[0]]
        b=[nums[1]]
        for i in nums[2:]:
            if a[-1]>b[-1]:
                a.append(i)
            else:
                b.append(i)
        return a+b
