class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(nums)
        nums[:]=sorted(list(set(nums)))
        return k