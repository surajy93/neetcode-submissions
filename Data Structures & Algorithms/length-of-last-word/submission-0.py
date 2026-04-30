class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list = s.split(" ")
        str_list = list(filter(None, str_list))
        n = len(str_list) - 1

        return len(str_list[n])
        