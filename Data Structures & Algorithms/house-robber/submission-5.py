class Solution:
    def rob(self, nums: List[int]) -> int:
        hashmap = {}

        def f(i,canRob):
            if i == len(nums):
                return 0
            if (i,canRob) in hashmap:
                return hashmap[(i,canRob)]
            
            if canRob == True:
                option1 = nums[i] + f(i+1,False)
                option2 = f(i+1,True)

                hashmap[(i,canRob)] = max(option1,option2)
            else:
                hashmap[(i,canRob)] = f(i+1,True)
                
            return hashmap[(i,canRob)]
        return f(0,True)