# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        temp = head
        nums =[]
        ans = []
        while temp:
            nums.append(temp)
            temp = temp.next
        
        dict = {}
        for node in nums:
            c = target - node.data
            if c in dict:
                ans.append((c,node.data))
            dict[node.data] = node
        
        ans.sort()
        return ans
                
            
        