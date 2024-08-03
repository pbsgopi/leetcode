class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(1, left):
            prev = prev.next
        curr = prev.next
        for i in range(right-left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next