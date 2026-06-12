class Solution:
    def longestConsecutive(self, num: List[int]) -> int:
        longestStreak = 0
        for i in num:
            if i - 1 not in num:
                currentStreak = 1
                while i + 1 in num:
                    currentStreak += 1
                    i += 1
                longestStreak = max(currentStreak, longestStreak)
        return longestStreak


        