# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ln = 0
        cur = head
        while cur:
            ln+=1
            cur = cur.next
        nth = ln - n

        c = 0
        cur = head
        prev = None
        if c==nth:
            head = head.next
            return head
        # 1 2 3 4
        while cur:
            if c==nth:
                prev.next = cur.next
                return head
            prev = cur
            c+=1
            cur = cur.next
        return head