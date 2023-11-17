class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #FIRST WE HAVE TO COUNT THE OCCURANCE IF ANY THING IS ACCORING THEN WE CAN MAKE POP THAT ELEMENT AND LOOK FOR THE NEXT ONE WITHT OLD ONE
        #FIRST COUNT THE ELEMETS GREATER THAN EQUAL TO TWO\
        count=1
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                count+=1
                if count>2:
                    nums.pop(i)
                else:
                    i+=1
            else:
                count=1
                i+=1
        return len(nums)
                    
                    
            
        