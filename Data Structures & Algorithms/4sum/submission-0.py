class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                tar = target - nums[i] - nums[j]
                left, right = j + 1, n - 1
                while left < right:
                    sum = nums[left] + nums[right]
                    if sum < tar:
                        left += 1
                    elif sum > tar:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]: right -= 1
                        while left < right and nums[left] == nums[left - 1]: left += 1
                while j + 1 < n and nums[j] == nums[j + 1]: j += 1
            while i + 1 < n and nums[i] == nums[i + 1]: i += 1

        return res

        