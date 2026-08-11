class Solution:
    def largestRectangleArea(self, heights):

        n = len(heights)

        # Previous Smaller
        pse = [-1] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                pse[i] = stack[-1]

            stack.append(i)

        # Next Smaller
        nse = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)
        #print(pse)
        #print(nse)
        # Calculate maximum area
        ans = 0

        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            ans = max(ans, area)

        return ans