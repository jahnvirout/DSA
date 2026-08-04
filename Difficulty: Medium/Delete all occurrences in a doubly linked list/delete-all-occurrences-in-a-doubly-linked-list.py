"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    def deleteAllOccurOfX(self, head, x):
        nums = []
        temp = head
        nums2 = []
        dummy = Node(0)
        
        
        while temp:
            nums.append(temp)
            temp = temp.next
        
        for i in range(len(nums)):
            if nums[i].data != x:
                nums2.append(nums[i])
        if not nums2:
            return None
        
        dummy.next = nums2[0]
        
        for j in range(len(nums2)-1):
            nums2[j].next = nums2[j+1]
            nums2[j+1].prev = nums2[j]
        
        nums2[-1].next = None
        nums2[0].prev = None
        return nums2[0]
        
            
        
        
        
        