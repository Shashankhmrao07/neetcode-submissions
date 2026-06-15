class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = 0
        freq = set()
        for i in range(len(s)):
            while s[i] in freq:
                freq.remove(s[l])
                l += 1
            freq.add(s[i])
            res = max(res, i - l + 1)
        return res

        