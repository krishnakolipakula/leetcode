class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)
        sum_int = a_int + b_int
        sum_binary = bin(sum_int)[2:]
        return sum_binary

