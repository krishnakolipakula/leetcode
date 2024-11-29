class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float("inf")
        left=0
        sum_curr=0
        for right in range(len(nums)):
            sum_curr+=nums[right]
            while sum_curr>=target:
                if right-left+1<min_len:
                    min_len=right-left+1
                sum_curr-=nums[left]
                left+=1
        return min_len if min_len!=float("inf") else 0

        
