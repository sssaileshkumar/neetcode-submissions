from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = counter.most_common(k)
        sol = []
        for a,b in ans:
            sol.append(a)
        return sol