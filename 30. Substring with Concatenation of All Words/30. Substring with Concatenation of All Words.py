from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or len(words[0]) == 0:
            return []

        word_len = len(words[0])
        word_count = len(words)
        word_map = Counter(words)
        result = []
        
        # Iterate through each possible starting point in the string
        for i in range(word_len):
            left = i
            right = i
            current_count = 0
            current_map = Counter()

            # Slide window through the string
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_map:
                    current_map[word] += 1
                    current_count += 1

                    # If the current word's frequency exceeds the required frequency, move left pointer
                    while current_map[word] > word_map[word]:
                        current_map[s[left:left + word_len]] -= 1
                        left += word_len
                        current_count -= 1

                    # If we have a valid substring, add the starting index
                    if current_count == word_count:
                        result.append(left)
                else:
                    # Reset window if the word is not in the word list
                    current_map.clear()
                    current_count = 0
                    left = right

        return result
