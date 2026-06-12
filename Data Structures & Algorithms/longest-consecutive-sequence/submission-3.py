class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestStreak = 0
        num = set(nums)
        for i in num:
            if i - 1 not in num:
                currentStreak = 1
                while i + 1 in num:
                    currentStreak += 1
                    i += 1
                longestStreak = max(currentStreak, longestStreak)
        return longestStreak


        