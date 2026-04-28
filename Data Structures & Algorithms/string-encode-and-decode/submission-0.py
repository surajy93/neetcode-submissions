class Solution:

    def encode(self, strs: List[str]) -> str:
        results = ""
        for s in strs:
            results += str(len(s)) + "#" + s
        return results

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delimiter_pos = s.find("#", i)
            length = int(s[i:delimiter_pos])
            start = delimiter_pos + 1
            end = start + length
            curr_str = s[start:end]
            result.append(curr_str)
            i = end
        return result


