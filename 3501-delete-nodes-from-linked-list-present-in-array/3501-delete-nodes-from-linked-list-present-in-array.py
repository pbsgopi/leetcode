class Solution:
    def modifiedList(self, a: List[int], h: Optional[ListNode]) -> Optional[ListNode]:
        def f(node, a={*a}):
            if node:
                if node.val in a:
                    return f(node.next)
                return ListNode(node.val, f(node.next))
        return f(h)