class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        res = []
        n = len(nums)

        for num in set(nums):
            if hashmap[num]>n//3:
                res.append(num)
        return res