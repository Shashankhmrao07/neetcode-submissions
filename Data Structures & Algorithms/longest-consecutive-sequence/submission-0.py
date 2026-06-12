class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestStreak = 0
        for i in nums:
            if i - 1 not in nums:
                currentStreak = 1
                while i + 1 in nums:
                    currentStreak += 1
                    i += 1
                longestStreak = max(currentStreak, longestStreak)
        return longestStreak


        