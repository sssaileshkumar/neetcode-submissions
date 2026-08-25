class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def is_matching(a,b):
            return a == "(" and b ==")" or a == "[" and b == "]" or a == "{" and b == "}"

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack or not is_matching(stack[-1],i):
                    return False
                stack.pop()
        
        return len(stack) == 0