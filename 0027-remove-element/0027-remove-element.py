class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i<=0:
            if val in nums:
                nums.remove(val)
            else:
                i=1
        return len(nums)
            
            
        