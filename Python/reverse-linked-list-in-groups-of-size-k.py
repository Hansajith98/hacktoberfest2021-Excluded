# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
        
        dummy = ListNode()
        dummy.next=head
        count = 0
        prev = curr = nex = dummy 
        
        # count the nodes in LL
        while curr.next:
            curr=curr.next
            count+=1
        
        # until non-reversed nodes in LL >= k
        while count>=k:
            curr = prev.next
            nex = curr.next
            # reverse k-nodes in place
            for i in range(1,k):
                # memorise/understand/create logic
                curr.next = nex.next
                nex.next = prev.next
                prev.next=nex
                nex=curr.next
            prev=curr
            # reduce count by k times - for exit condition
            count-=k
                
        
        return dummy.next
