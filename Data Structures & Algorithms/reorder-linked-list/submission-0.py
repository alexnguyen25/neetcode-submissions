class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Split and reverse second half
        l2 = slow.next
        slow.next = None

        prev = None
        curr = l2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l2 = prev

        # 3. Merge the two halves
        l1 = head
        while l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next