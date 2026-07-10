class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxLen = left = 0
        for right in range(len(nums)):
            while right - left + 1 == k:
                maxLen = max(nums[left:right + 1])
                res.append(maxLen)
                left += 1
        return res
            
            
        