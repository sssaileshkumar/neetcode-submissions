class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = "".join(i.lower() for i in s if i.isalnum())
        return temp == temp[::-1]