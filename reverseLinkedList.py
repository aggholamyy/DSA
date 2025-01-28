Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Reverses a singly linked list using recursion.

    Parameters:
        head (Optional[ListNode]): The head of the singly linked list.

    Returns:
        Optional[ListNode]: The new head of the reversed linked list.

    The function traverses to the end of the list recursively, then reverses the links
    as the recursion unwinds, ensuring that all nodes point to their previous node
    in the original list. The new head of the reversed list is returned.
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        else:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_head
        
       