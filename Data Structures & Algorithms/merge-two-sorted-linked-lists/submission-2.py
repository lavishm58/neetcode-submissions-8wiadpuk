# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nw = None
        if list1 and list2:
            if list1.val <=list2.val:
                nw = ListNode(list1.val)
                list1 = list1.next
            else:
                nw = ListNode(list2.val)
                list2 = list2.next
        elif not list1 and list2:
            nw = ListNode(list2.val)
            list2 = list2.next
        elif not list2 and list1:
            nw = ListNode(list1.val)
            list1 = list1.next
        elif not list1 and not list2:
            return None
        final = nw
        # print(final.val, 'dfv')
        while list1 or list2:
            if list1 and list2:
                if list1.val <=list2.val:           
                    nw.next = list1
                    list1 = list1.next
                else:
                    nw.next = list2
                    list2 = list2.next

            elif not list1 and list2:
                nw.next = list2
                list2 = list2.next

            elif list1 and not list2:
                nw.next = list1
                list1 = list1.next
            
            nw = nw.next

        return final