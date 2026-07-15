class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        left = 0
        right = k-1

        while right<len(nums):
            if right-left+1>k:
                left+=1
            right += 1
            output.append(max(nums[left:right]))
        return output