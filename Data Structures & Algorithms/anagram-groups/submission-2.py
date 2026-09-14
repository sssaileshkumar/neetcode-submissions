class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} #index(key) : anagrams

        for word in strs:
            key = "".join(s for s in sorted(word))

            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(word)
        return list(hashmap.values())
