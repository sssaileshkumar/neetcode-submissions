class Solution(object):
    def maxSubArray(self, nums):
        ans = nums[0]
        temp = 0

        for num in nums:
            temp += num
            ans = max(ans,temp)

            if temp<0:
                temp = 0
        return ans
