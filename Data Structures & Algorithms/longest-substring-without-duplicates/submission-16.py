class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()

        left = 0
        right = 0
        temp = ans = 1

        while right<len(s):
            if s[right] not in seen:
                seen.add(s[right])
                temp = right-left+1
                right += 1
            else:
                seen.remove(s[left])
                left += 1
            ans = max(ans,temp)
        return ans