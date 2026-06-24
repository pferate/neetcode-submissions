# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next = None
        last_node = None
        while True:
            if head is None:
                break
            # print(f"head.val: {head.val}, head.next: {head.next}")
            next = head.next
            head.next = last_node
            # print(f"head.val: {head.val}, head.next: {head.next}, next: {next}")
            if next is None:
                break
            last_node = head
            head = next
        return head
        