class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = "".join(str(digit) for digit in digits)
        ans = int(number)+1
        res = []
        for i in str(ans):
            res.append(int(i))
        return res