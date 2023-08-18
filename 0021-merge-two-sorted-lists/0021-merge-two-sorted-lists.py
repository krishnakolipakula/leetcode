# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        k=ListNode()
        d=k
        while list1 and list2 :
            if list1.val<list2.val:
                d.next=list1
                list1=list1.next
            else:
                d.next=list2
                list2=list2.next    
            d=d.next
        if list1:
            d.next=list1
        elif list2:
            d.next=list2
        return k.next           