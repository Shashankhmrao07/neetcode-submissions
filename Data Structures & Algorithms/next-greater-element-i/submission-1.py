class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack = []
        # nge = {}

        # for num in nums2:
        #     while stack and stack[-1] < num:
        #         nge[stack.pop()] = num

        #     stack.append(num)

        # return [nge.get(num, -1) for num in nums1]

        nge = {}
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()
            
            nge[num] = stack[-1] if stack else -1
            stack.append(num)

        return [nge.get(num, -1) for num in nums1]