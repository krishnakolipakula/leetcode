class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        i, j = 0, 0  
        max_length = 0  
        while j < len(s):
            if s[j] in hashmap and hashmap[s[j]] != 0:
                hashmap = {}
                i += 1  
                j = i  
            else:
                hashmap[s[j]] = 1
                max_length = max(max_length, j - i + 1)
                j += 1
        return max_length
