class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Base case
        if not head or not head.next:
            return head

        # Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge two sorted lists
        return self.merge(left, right)

    def merge(self, l1, l2):

        dummy = ListNode(0)
        temp = dummy

        while l1 and l2:

            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        if l1:
            temp.next = l1
        else:
            temp.next = l2

        return dummy.next