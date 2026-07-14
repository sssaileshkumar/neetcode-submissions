class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        temp = ans = 0

        while left<right:
            temp = min(heights[left],heights[right])*(right-left)
            ans = max(temp,ans)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return ans        