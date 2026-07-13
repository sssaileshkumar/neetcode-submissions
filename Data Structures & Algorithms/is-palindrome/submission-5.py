class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(i.lower() for i in s if i.isalnum())
        return word == word[::-1]