class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, v in enumerate(nums):
            x = target - v
            if x in h:
                return [h[x], i]
            h[v] = i

        