# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #brute

        temp = head
        visited = set()
        
        while temp:
            if temp in visited:
                return temp
            visited.add(temp)
            temp = temp.next
        return None