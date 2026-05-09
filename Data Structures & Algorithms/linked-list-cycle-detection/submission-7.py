# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hmap = {}
        cur = head
        while cur:
            if cur in hmap:
                return True
            else:
                hmap[cur] = 1
            cur = cur.next
        return False
        