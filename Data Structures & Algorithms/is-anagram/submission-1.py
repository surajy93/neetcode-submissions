class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for w in s:
            if w not in s_freq:
                s_freq[w] = 1
            else:
                s_freq[w] += 1
     
        for w in t:
            if w not in t_freq:
                t_freq[w] = 1
            else:
                t_freq[w] += 1
        return s_freq == t_freq

