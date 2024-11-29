## Minimal Length Subarray with Sum Constraint

### Problem Statement
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If no such subarray exists, return `0`.

---

### Examples

#### Example 1
**Input:**  
`target = 7`, `nums = [2,3,1,2,4,3]`  
**Output:**  
`2`  
**Explanation:** The subarray `[4,3]` has the minimal length under the problem constraint.

#### Example 2
**Input:**  
`target = 4`, `nums = [1,4,4]`  
**Output:**  
`1`  
**Explanation:** The subarray `[4]` meets the condition.

#### Example 3
**Input:**  
`target = 11`, `nums = [1,1,1,1,1,1,1,1]`  
**Output:**  
`0`  
**Explanation:** No subarray meets the condition.

---

### Constraints
- \( 1 \leq \text{target} \leq 10^9 \)
- \( 1 \leq \text{nums.length} \leq 10^5 \)
- \( 1 \leq \text{nums[i]} \leq 10^4 \)
