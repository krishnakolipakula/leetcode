# Explanation of the Solution

This Python solution solves **Two Sum II - Input Array Is Sorted** using the **Two Pointer Technique**. The logic ensures that the problem is solved efficiently with \(O(n)\) time complexity.

## Code Breakdown

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Initialize two pointers: left (l) and right (r)

        while l < r:  # Continue until the two pointers meet
            cursum = numbers[l] + numbers[r]  # Calculate the sum of the two numbers

            if cursum > target:
                r -= 1  # Move the right pointer left to reduce the sum
            elif cursum < target:
                l += 1  # Move the left pointer right to increase the sum
            elif cursum == target:
                return [l + 1, r + 1]  # Return 1-based indices if the target sum is found
```
# Steps:
## Initialize Two Pointers:

l points to the start of the array.
r points to the end of the array.
Calculate Current Sum (cursum):

The sum of the elements at the l and r pointers is stored in cursum.
Adjust Pointers Based on cursum:

**If cursum is greater than the target, reduce the sum by moving the right pointer (r) left.**

**If cursum is less than the target, increase the sum by moving the left pointer (l) right.**

**If cursum matches the target, return the indices of the numbers as a list (1-based format).**

## Return the Result:


Return [l + 1, r + 1] when the cursum matches the target.

## Key Features
Input Assumption:

The input array numbers is sorted in non-decreasing order, enabling the use of the two-pointer technique.
Time Complexity:
𝑂
(
𝑛
)
O(n), as each pointer traverses the array at most once.

Space Complexity:
𝑂
(
1
)
O(1), as no extra space is used apart from the pointers.
