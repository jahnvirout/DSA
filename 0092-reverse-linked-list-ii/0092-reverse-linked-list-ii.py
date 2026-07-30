# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next  #temp has 3
            curr.next = temp.next  #2 points to 4
            temp.next = prev.next  # 3 points to 2
            prev.next = temp
        
        return dummy.next





        