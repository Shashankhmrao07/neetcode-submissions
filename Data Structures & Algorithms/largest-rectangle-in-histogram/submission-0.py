class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                element = stack.pop()
                nse = i
                pse = stack[-1] if stack else -1
                maxArea = max(maxArea, (heights[element] * (nse - pse - 1)))
            stack.append(i)

        while stack:
            nse = n
            element = stack.pop()
            pse = stack[-1] if stack else -1
            maxArea = max(maxArea, (heights[element] * (nse - pse - 1)))
        return maxArea

        