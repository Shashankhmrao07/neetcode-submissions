class Solution:
    def leftmax(self, height):
        prefix = [0] * len(height)
        prefix[0] = height[0]
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i])

        return prefix

    def rightmax(self, height):
        n = len(height)
        suffix = [0] * n
        suffix[n-1] =  height[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])

        return suffix


    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(len(height)):
            leftmax, rightmax = self.leftmax(height), self.rightmax(height)
            if leftmax[i] > height[i] and rightmax[i] > height[i]:
                total += min(leftmax[i], rightmax[i]) - height[i]

        return total
        