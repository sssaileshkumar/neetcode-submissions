class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def age(string):
            return int(string[11:13])
        ans = 0

        for detail in details:
            if age(detail)>60:
                ans += 1
        return ans