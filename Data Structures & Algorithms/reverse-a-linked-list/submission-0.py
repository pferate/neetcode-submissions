# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        while True:
            if head is None:
                break
            # print(f"head.val: {head.val}, Reversed: {reversed}")
            reversed = ListNode(head.val, reversed)
            # print(f"Adding: {reversed}, reversed.val: {reversed.val}, reversed.next: {reversed.next}")
            head = head.next
        return reversed
        