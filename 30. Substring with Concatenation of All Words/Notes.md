## Explanation of the Solution

The problem asks to find all the starting indices of concatenated substrings in the string `s` that are permutations of a given list of words. The key observation is that the substrings we are looking for are **concatenations of permutations** of the words in the list.

### Approach

1. **Basic Idea:**
   - Each word in the list `words` has the same length.
   - The concatenated substring we are searching for will be of the length `len(words) * len(word)` (since each word in `words` has the same length).
   - We need to check every substring of `s` that has this total length and see if it contains all the words in `words` in some permutation.

2. **Sliding Window Approach:**
   - Use a sliding window of size equal to the total length of all words concatenated (i.e., `len(words) * len(word)`).
   - Slide this window across the string `s` to examine every potential substring of the required length.

3. **Word Frequency Matching:**
   - We maintain a `Counter` (hashmap) to track the frequency of each word in `words`.
   - As we slide the window, we extract words from the substring and keep track of their counts in another `Counter`.
   - If the counts of words in the current window match the counts in `words`, then the substring is a valid concatenation of some permutation of `words`.

4. **Efficient Search with Sliding Window:**
   - For each starting index in `s`, we initialize the window and begin comparing words.
   - If a word is not part of `words`, we reset the window.
   - If a word appears more times than required, we shrink the window from the left by moving the left pointer.

5. **Handling Edge Cases:**
   - If the total length of `words` exceeds the length of `s`, no valid substrings are possible, and the result is an empty list.
   - If the `words` array is empty, return an empty list as well.

### Code Walkthrough:

1. **Initialization:**
   - We calculate the length of each word and the number of words in `words`.
   - We create a frequency map (`word_map`) for the words in `words`.

2. **Sliding Window Logic:**
   - We slide the window starting from each index within the length of a single word (`i = 0` to `word_length-1`) to account for all possible starting positions.
   - Within each sliding window, we track how many words match the frequency map and adjust the window if there are too many occurrences of a word.

3. **Final Output:**
   - Once we find a valid window (i.e., when the window contains all words in the correct frequency), we add the starting index of that window to the result list.

### Time Complexity:
- **O(n * m)**, where `n` is the length of `s` and `m` is the length of each word in `words`. The sliding window iterates through `n` with checks that involve a fixed amount of work for each word (checking its frequency).
  
### Space Complexity:
- **O(k)**, where `k` is the number of words in `words`. We need extra space for storing the word counts (`word_map` and `current_map`).

### Code Example:
```python
from collections import Counter

def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []
    
    word_length = len(words[0])
    word_count = len(words)
    word_map = Counter(words)
    result = []
    
    # Traverse the string and check every substring of length word_length * word_count
    for i in range(word_length):
        left = i
        right = i
        current_count = 0
        current_map = Counter()
        
        while right + word_length <= len(s):
            word = s[right:right + word_length]
            right += word_length
            
            if word in word_map:
                current_map[word] += 1
                current_count += 1
                
                # Shrink the window if we have more occurrences of the word than required
                while current_map[word] > word_map[word]:
                    left_word = s[left:left + word_length]
                    current_map[left_word] -= 1
                    current_count -= 1
                    left += word_length
                
                # If current_count equals the number of words, we found a valid substring
                if current_count == word_count:
                    result.append(left)
            else:
                # Reset the window if the word is not part of words
                current_map.clear()
                current_count = 0
                left = right
    
    return result
