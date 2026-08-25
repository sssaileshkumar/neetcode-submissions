class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        stack = []

        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                index = stack.pop()
                res[index] = i-index
            stack.append(i)
        return res