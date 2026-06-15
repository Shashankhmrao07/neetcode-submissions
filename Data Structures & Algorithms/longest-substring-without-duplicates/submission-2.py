class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = 0
        freq = set()
        for i, v in enumerate(s):
            while v in freq:
                freq.remove(s[l])
                l += 1
            freq.add(v)
            res = max(res, i - l + 1)
        return res