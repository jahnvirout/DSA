# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        temp  = head
        while temp:
            arr.append(temp)
            temp = temp.next
        idx = len(arr) - n

        if idx == 0:
            return head.next
        elif idx == len(arr)-1:
            arr[idx-1].next = None
        else:
            arr[idx-1].next = arr[idx+1]
        
        return head
        


