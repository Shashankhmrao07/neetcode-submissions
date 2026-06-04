class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        # for i in asteroids:
        #     if i > 0:
        #         stack.append(i)
        #     else:
        #         while stack and stack[-1] < abs(i) and stack[-1] > 0:
        #             stack.pop()
        #         if stack and stack[-1] == abs(i):
        #             stack.pop()
        #         elif not stack or stack[-1] < 0:
        #             stack.append(i)
        # return stack
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
        