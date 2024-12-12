# Longest Substring Without Repeating Characters

This problem aims to find the length of the longest substring in a given string `s` without repeating characters. The solution is implemented using a **sliding window** technique, utilizing a **hashmap** to track the characters in the current window. The algorithm moves through the string while adjusting the window to ensure no duplicate characters are included in the substring.

## Problem Description

Given a string `s`, return the length of the **longest substring** without repeating characters.

### Example:

Input: `"abcabcbb"`

Output: `3`  
Explanation: The answer is `"abc"`, with the length of `3`.

## Solution Explanation

The provided solution uses the **sliding window** approach to efficiently find the length of the longest substring without repeating characters. Let’s break down the code:

### Key Concepts:

1. **Sliding Window Technique**: This technique allows you to dynamically manage a window of characters that are being processed. The window expands or contracts based on certain conditions (in this case, the appearance of duplicate characters).
   
2. **HashMap (Dictionary)**: We use a hashmap (or dictionary) to keep track of the characters in the current window. The hashmap stores characters as keys and their corresponding counts or indices as values. This allows for efficient look-up and update operations.

### Code Walkthrough

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}  # A dictionary to store the characters in the current window
        i, j = 0, 0  # Two pointers, i (left) and j (right) to represent the window
        max_length = 0  # Variable to track the maximum length of the substring
        
        while j < len(s):  # Iterate through the string with the right pointer `j`
            if s[j] in hashmap and hashmap[s[j]] != 0:  
                # If a duplicate character is found in the window
                hashmap = {}  # Clear the hashmap (reset the window)
                i += 1  # Move the left pointer `i` forward to avoid duplicates
                j = i  # Reset the right pointer `j` to start a new window from `i`
            else:
                hashmap[s[j]] = 1  # Add/update the character in the hashmap
                max_length = max(max_length, j - i + 1)  # Update the max length
                j += 1  # Move the right pointer `j` forward to expand the window
        
        return max_length  # Return the maximum length of the substring
