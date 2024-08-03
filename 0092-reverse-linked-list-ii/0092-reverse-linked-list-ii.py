class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst=[]
        curr=head
        while curr:
            lst.append(curr.val)        
            curr=curr.next
        while left<right:
            lst[left-1],lst[right-1]=lst[right-1],lst[left-1]
            left+=1
            right-=1
        curr=ans=ListNode()
        for i in lst:
            curr.next=ListNode(i)
            curr=curr.next
        return ans.next