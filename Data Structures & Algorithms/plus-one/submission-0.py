class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        plusone, i = 1, 0
        while plusone:
            if i < len(digits):
                if digits[i] == 9:
                    plusone = 1
                    digits[i] = 0
                else:
                    digits[i] += 1
                    plusone = 0
            else:
                digits.append(plusone)
                plusone = 0
            i += 1
        return digits[::-1]