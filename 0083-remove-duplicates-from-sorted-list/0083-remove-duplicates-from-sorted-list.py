# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        if prev and prev.next:
            temp=prev.next
            while temp and temp.next:
                if prev.val==temp.val:
                    prev.next=temp.next
                    temp=prev.next
                else:
                    prev=prev.next
                    temp=temp.next
            if prev.val==temp.val:
                    prev.next=temp.next
        return head
                
                
            
                
            
        
        
        