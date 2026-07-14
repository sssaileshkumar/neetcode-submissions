class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        ans = 0

        left = 0
        right = 0

        while right < len(s):
            hashmap[s[right]] = 1 + hashmap.get(s[right], 0)

            while (right - left + 1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans