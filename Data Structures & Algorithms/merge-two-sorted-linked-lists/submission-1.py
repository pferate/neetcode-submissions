# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        starting = ListNode()
        curr1 = list1
        curr2 = list2
        current = starting
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                current.next = curr1
                curr1 = curr1.next
            else:
                current.next = curr2
                curr2 = curr2.next
            current = current.next
        if curr1:
            current.next = curr1
        else:
            current.next = curr2
        # Skip the dummy head
        return starting.next