class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = ans = 0

        for right in range(len(s)):
            if s[right] not in hashmap:
                hashmap[s[right]] = 0
            hashmap[s[right]] += 1

            while (right-left+1)-max(hashmap.values())>k:
                hashmap[s[left]] -= 1
                left += 1
            
            ans = max(ans,right-left+1)
        return ans