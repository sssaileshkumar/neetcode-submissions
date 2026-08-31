class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        num = 0

        for i in range(len(s)-1):
            if hashmap[s[i]] < hashmap[s[i+1]]:
                num -= hashmap[s[i]]
            else:
                num += hashmap[s[i]]
        return num + hashmap[s[-1]]