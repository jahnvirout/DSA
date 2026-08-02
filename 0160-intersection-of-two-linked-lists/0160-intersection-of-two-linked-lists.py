# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp = headA
        lenA = 0
        lenB = 0
        tempA = headA
        tempB = headB
        while tempA:
            lenA+=1
            tempA = tempA.next

        while tempB:
            lenB+=1
            tempB = tempB.next
        
        tempA = headA
        tempB = headB
        
        if lenA>lenB:
            d = lenA - lenB
            temp = headA
            for _ in range(d):
                tempA = tempA.next
        else:
            d = lenB - lenA
            tempB = headB
            for _ in range(d):
                tempB = tempB.next
        
        while tempA or tempB:
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next
            
        return None

  
        
        

        


