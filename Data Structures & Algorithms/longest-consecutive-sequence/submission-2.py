class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seen = set()
        temp = ans = 0

        for num in nums:
            if num-1 not in seen:
                temp = 0
                current_num = num
                while current_num in nums:
                    seen.add(current_num)
                    temp += 1
                    current_num += 1
                ans = max(ans,temp)
        return ans