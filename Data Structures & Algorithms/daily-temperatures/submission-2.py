class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []
        for i, v in enumerate(temp):
            while stack and v > stack[-1][0]:
                stacktemp, stackindex = stack.pop()
                res[stackindex] = i - stackindex
            stack.append([v, i])
        return res

        