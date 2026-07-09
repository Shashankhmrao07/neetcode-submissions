class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        minLen = 10 ** 9
        count = left = 0
        lIndex = rIndex = -1
        if t == "" or len(t) > len(s):
            return ""
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        for right in range(len(s)):
            if freq.get(s[right], 0) > 0:
                count += 1
            freq[s[right]] = freq.get(s[right], 0) - 1
            while len(t) == count:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    lIndex, rIndex = left, right

                freq[s[left]] += 1
                if freq[s[left]] > 0:
                    count -= 1
                left += 1
        return "" if lIndex == -1 else s[lIndex:rIndex + 1] 
        