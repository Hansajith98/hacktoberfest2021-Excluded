
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        fast = slow = head
        # if there's a cylce the fast and slow ptr will meet at some point
        while fast and fast.next:
            fast = fast.next.next
            slow=slow.next
            if fast == slow:
                return True
        
        return False
