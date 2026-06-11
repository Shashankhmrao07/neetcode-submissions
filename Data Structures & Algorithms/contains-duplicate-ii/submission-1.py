class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # window = set()
        # l = 0

        # for r in range(len(nums)):
        #     if r - l > k:
        #         window.remove(nums[l])
        #         l += 1
        #     if nums[r] in window:
        #         return True
        #     window.add(nums[r])
        # return False

        if len(nums) == len(set(nums)):
            return False
        else:
            for i in range(len(nums)):
                if nums[i] in nums[i+1:i+1+k]:
                    return True
            return False