class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [0]*n
        right[-1] = -1

        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],nums[i+1])
        
        return right