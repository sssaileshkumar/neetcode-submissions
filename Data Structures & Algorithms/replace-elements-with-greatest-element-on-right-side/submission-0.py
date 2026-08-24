class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        right = [0]*n
        right[-1] = arr[-1]

        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],arr[i+1])
        
        right[-1] = -1

        return right