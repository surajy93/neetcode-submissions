class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(clean_s) - 1
        while i <= j:
            if clean_s[i] == clean_s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
            
        