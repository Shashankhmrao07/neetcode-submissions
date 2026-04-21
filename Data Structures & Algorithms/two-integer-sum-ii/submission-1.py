class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i in numbers:
            x = target - i
            if x in numbers:
                if i > x:
                    return [numbers.index(x)+1, numbers.index(i)+1]
                else:
                    return [numbers.index(i)+1, numbers.index(x)+1]
        