class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst =  [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            lst[ord(s[i])-97] += 1
            lst[ord(t[i])-97] -= 1

        for x in lst:
            if x != 0:
                return False
        return True
        

        