class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, return the length of the longest substring without repeating characters.
        :param s: a string
        :return: length of longest substring without repeats
        """
        if not s:
            return 0
        char_map = {}
        result = float("-inf")
        i, j = 0, 0
        while j < len(s):
            if s[j] not in char_map:
                char_map[s[j]] = 0
                result = max(result, len(char_map))
                j += 1
            else:
                del char_map[s[i]]
                i += 1
        return result
