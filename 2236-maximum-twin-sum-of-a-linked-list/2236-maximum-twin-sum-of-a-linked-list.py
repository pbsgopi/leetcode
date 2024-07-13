# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        res=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        for i in range(len(arr)):
            a=arr[i]+arr[len(arr)-1-i]
            res.append(a)
        return max(res)