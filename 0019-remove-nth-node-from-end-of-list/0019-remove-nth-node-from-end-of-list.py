# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=head
        c,count=1,1
        while k.next!=None:
            k=k.next
            count+=1
        k=head
        p=head
        while c!=(count-n+1):
            p=k
            k=k.next
            c+=1
        if count==1:
            head=None
            return head
        if count==2:
            if n==1:
                head.next=None
                return head
            head=head.next
            return head
        if count-n==0:
            head=head.next
            return head
        p.next=k.next
        return head
        