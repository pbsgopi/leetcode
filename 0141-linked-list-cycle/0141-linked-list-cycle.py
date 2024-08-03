class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return False
        slow=head
        fast=head.next
        while fast!=None:
            if fast==slow:
                return True
            else:
                slow=slow.next
                fast=fast.next
                if fast!=None:
                    fast=fast.next
        return False