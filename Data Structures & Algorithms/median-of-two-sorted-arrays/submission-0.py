class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0
        res = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while j < n:
            res.append(nums2[j])
            j += 1

        while i < m:
            res.append(nums1[i])
            i += 1

        l = len(res)
        if l % 2 != 0:
            result = res[(l-1)//2]
        else:
            result = float(res[l//2] + res[l//2 - 1]) / 2
        return result




        