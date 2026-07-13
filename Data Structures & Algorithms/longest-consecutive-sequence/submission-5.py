class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        seen = set(nums)
        temp = 1

        for num in nums:
            if num-1 not in seen:
                temp = 1
                while num+1 in seen:
                    temp+=1
                    num+=1
                ans = max(temp,ans)
        return ans