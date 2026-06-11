class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        res = []
        n = len(arr) - 1
        arr.sort()
        for i in range(n - 1):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            j, k = i + 1, n
            while j < k:
                sum = arr[i] + arr[j] + arr[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    res.append([arr[i], arr[j], arr[k]])
                    j += 1
                    k -= 1
                    while (j < k and arr[j] == arr[j - 1]):
                        j += 1
                    while (j < k and arr[k] == arr[k + 1]):
                        k -= 1
                    
        return res
