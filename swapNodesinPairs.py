class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
      """
      1. First, we swap the first two nodes in the list, i.e. head and head.next;
      2. Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
      3. Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.
      """
      if (not head) or (not head.next):
        return head
      else:
        current_head = head
        next_head = head.next.next
        head = head.next
        head.next = current_head
        head.next.next = self.swapPairs(next_head)
        return head