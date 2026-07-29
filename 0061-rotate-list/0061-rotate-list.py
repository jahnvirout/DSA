# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # Find length
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        k = k % length

        if k == 0:
            return head

        # Rotate one step, k times
        for _ in range(k):

            prev = None
            temp = head

            while temp.next:
                prev = temp
                temp = temp.next

            temp.next = head
            head = temp
            prev.next = None

        return head