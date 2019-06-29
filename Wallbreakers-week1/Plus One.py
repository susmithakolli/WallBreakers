class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b = []
        for item in range(len(digits)):
            digits[item] = str(digits[item])
            
        a = "".join(digits)
        a = int(a)
        a += 1
        for item in str(a):
            b.append(int(item))
        return b 