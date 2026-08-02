# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head1
        temp2 = head2
        dummy = ListNode(0)
        temp = dummy
        
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
                temp = temp.next
            else:
                temp.next = temp2
                temp2 = temp2.next
                temp = temp.next
        
        if temp1:
            temp.next = temp1
        else:
            temp.next = temp2
        return dummy.next