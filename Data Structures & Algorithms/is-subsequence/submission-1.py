class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps , pt = 0 , 0
        res = ""
        while pt <= len(t) - 1 and ps <= len(s) - 1:
            if s[ps] == t[pt]:
                res += s[ps]
                ps += 1
                pt += 1
            else:
                pt += 1
        return res == s



                
        