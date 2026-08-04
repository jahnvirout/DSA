# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        nums = []
        nums2 = []
        while temp:
            nums.append(temp)
            temp = temp.next
        
        #array = [1 2 6 3 4 5 6]
        for i in range(len(nums)):
            if nums[i].val!=k:
                nums2.append(nums[i])
        
        if not nums2:
            return None
            
        for j in range(len(nums2)-1):
            nums2[j].next = nums2[j+1]
        
        nums2[-1].next = None
        return nums2[0]
      



