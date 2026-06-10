class Solution:
    def getSum(self, a: int, b: int) -> int:
        k = 32
        while b and k:
            k -= 1
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        if k == 0:
            return a&0xFFFFFFFF
        return a
