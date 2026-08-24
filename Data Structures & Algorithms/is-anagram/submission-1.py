class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hashify(string):
            hashmap = {}

            for i in string:
                if i in hashmap:
                    hashmap[i] += 1
                else:
                    hashmap[i] = 1
            return hashmap
        
        return hashify(s) == hashify(t)