class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = ''.join(map(str, digits))
        k=int(k)+1
        digit_list = [int(digit) for digit in str(k)]
        return digit_list