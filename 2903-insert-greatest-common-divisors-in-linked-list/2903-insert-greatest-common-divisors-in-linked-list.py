# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr.next:
            new=ListNode()
            new.val=math.gcd(curr.val,curr.next.val)
            next=curr.next
            curr.next=new
            new.next=next
            curr=curr.next.next
        return head