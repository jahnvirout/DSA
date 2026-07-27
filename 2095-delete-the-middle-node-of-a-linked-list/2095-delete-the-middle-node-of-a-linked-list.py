# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        if head.next is None:
            return None

        while temp!=None:
            arr.append(temp)
            temp = temp.next
    
        mid = len(arr)//2
        
        if mid == len(arr)-1:
            arr[mid-1].next = None
        else:
            arr[mid-1].next = arr[mid+1]
        
        return head
        
