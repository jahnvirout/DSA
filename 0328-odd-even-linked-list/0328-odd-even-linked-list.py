# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head
        arr = []
        while temp:
            arr.append(temp)
            temp = temp.next
        
        newArr = []
        
        for i in range(0,len(arr),2):   #odd
            newArr.append(arr[i])
        for i in range(1,len(arr),2):   #even 
            newArr.append(arr[i])

        for i in range(len(newArr)-1):
            newArr[i].next = newArr[i+1]
        if not newArr:
           return None
        
        newArr[-1].next = None
        return newArr[0]
        