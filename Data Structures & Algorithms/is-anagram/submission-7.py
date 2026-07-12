class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hashify(word):
            hashmap = {}
            for letter in word:
                if letter not in hashmap:
                    hashmap[letter] = 1
                else:
                    hashmap[letter] += 1
            return hashmap
        
        return hashify(s) == hashify(t)
