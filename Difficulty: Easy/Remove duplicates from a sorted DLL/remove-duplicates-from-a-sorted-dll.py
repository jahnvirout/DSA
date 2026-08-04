# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        prev = None
        curr = headRef
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
                if curr.next:
                    curr.next.prev = curr
                
            else:
                curr = curr.next
        return headRef
        
       