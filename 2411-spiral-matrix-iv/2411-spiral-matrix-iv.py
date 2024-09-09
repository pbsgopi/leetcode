# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1]*n for _ in range(m)]
        x, y = 0, 0
        dx, dy = 1, 0
        current = head
        while current:
            result[y][x] = current.val
            if y+dy<0 or y+dy>=m or x+dx<0 or x+dx>=n or result[y+dy][x+dx]>=0:
                dx, dy = -dy, dx
            y+=dy
            x+=dx
            current = current.next
        return result