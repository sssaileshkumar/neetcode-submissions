class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = right = 0
        ans = 0

        while left<len(s) and right<len(s):
            if s[right] not in seen:
                seen.add(s[right])
                ans = max(ans,right-left+1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return ans