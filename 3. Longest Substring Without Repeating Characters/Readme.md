# Longest Substring Without Repeating Characters

This problem requires you to find the length of the **longest substring** in a given string `s` without repeating characters. The solution is implemented using the **sliding window** technique, utilizing a **hashmap** to track characters in the current window, and adjusting the window size dynamically.

## Problem Description

Given a string `s`, return the length of the **longest substring** without repeating characters.

### Example 1:

Input: `"abcabcbb"`

Output: `3`  
Explanation: The answer is `"abc"`, with the length of `3`.

### Example 2:

Input: `"bbbbb"`

Output: `1`  
Explanation: The answer is `"b"`, with the length of `1`.

### Example 3:

Input: `"pwwkew"`

Output: `3`  
Explanation: The answer is `"wke"`, with the length of `3`.  
Notice that the answer must be a substring, `"pwke"` is a subsequence, not a substring.

### Constraints:
- `0 <= s.length <= 5 * 10^4`
- `s` consists of **English letters**, **digits**, **symbols**, and **spaces**.

## Solution Explanation

The solution uses the **sliding window** technique to find the longest substring without repeating characters. A **hashmap** (or dictionary) is used to track the characters in the window, and the window expands or contracts based on the presence of duplicate characters.

### Code Walkthrough:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}  # Dictionary to store characters and their positions in the string
        i, j = 0, 0  # Two pointers to represent the window (i = left, j = right)
        max_length = 0  # Variable to track the maximum length of the substring
        
        while j < len(s):  # Iterate through the string with the right pointer `j`
            if s[j] in hashmap and hashmap[s[j]] >= i:  
                # If character at `s[j]` is already in the window
                i = hashmap[s[j]] + 1  # Move the left pointer `i` right after the previous occurrence of `s[j]`
            
            hashmap[s[j]] = j  # Update the position of `s[j]` in the hashmap
            max_length = max(max_length, j - i + 1)  # Update the max length of the substring
            j += 1  # Move the right pointer `j` forward to expand the window
        
        return max_length  # Return the maximum length of the substring
