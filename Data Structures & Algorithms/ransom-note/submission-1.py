from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hasha = Counter(ransomNote)
        hashb = Counter(magazine)

        for i in hasha:
            if hasha[i] > hashb[i]: #need not be equal.
                return False
        return True