class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a=ListNode(0)
        b=ListNode(0)
        curr1=a
        curr2=b
        while head:
            if head.val<x:
                curr1.next,curr1=head,head
            else:
                curr2.next,curr2=head,head
            head=head.next
        curr2.next=None
        curr1.next=b.next
        return a.next