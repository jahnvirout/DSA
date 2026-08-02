# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        arr.sort()

        dummy = ListNode(0)
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next