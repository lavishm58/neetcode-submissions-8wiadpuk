# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 2 3
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None

        prev = None

        while fast: 
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp
        
        fast = prev
        slow = head
        # print(slow.val, fast.val)
        while slow and fast:
            tmp1, tmp2 = slow.next, fast.next
            slow.next = fast
            fast.next = tmp1
            slow, fast = tmp1, tmp2
