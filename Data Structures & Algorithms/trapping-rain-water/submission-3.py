class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0]*n
        right = [0]*n
        left[0] = heights[0]
        right[-1] = heights[-1]

        for i in range(1,n):
            left[i] = max(left[i-1],heights[i])
        
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],heights[i])
        
        #print(left)
        #print(right)

        ans = 0

        for i in range(n):
            ans += (min(left[i],right[i])-heights[i])
        return ans