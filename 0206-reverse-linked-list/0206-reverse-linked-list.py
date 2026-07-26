# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        arr = []

        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        arr.reverse()

        temp = head
        i = 0

        while temp:
            temp.val = arr[i]
            i += 1
            temp = temp.next

        return head