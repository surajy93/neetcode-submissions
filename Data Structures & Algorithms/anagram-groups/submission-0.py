class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            sorted_key = tuple(sorted(word))
            anagram_dict[sorted_key].append(word)
        return list(anagram_dict.values())

            