import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        y = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if y == y[::-1]:
            return True
        else:
            return False
    