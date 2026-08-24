class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = ans = 0

        for num in nums:
            if num == 1:
                temp += 1
                ans = max(temp,ans)
            else:
                 temp = 0
        return ans