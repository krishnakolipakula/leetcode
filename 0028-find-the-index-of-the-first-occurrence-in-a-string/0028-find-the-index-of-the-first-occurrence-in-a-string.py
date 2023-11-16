class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try :
            res=haystack.index(needle)
            return res
        except ValueError :
            return -1
        