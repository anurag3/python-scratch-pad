# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Soln 1 Iteratively (using references) -
    We can use 2 pointer method. One pointer "Current" and "Prev".
    We store the current pointer.next to a var, then update current pointer.next to point to prev node
    Then move the prev node to current node and finally move the current to next node with the stored var

    Time complexity is O(n) since we have to traverse through all the elements atleast once and
    Space Complexity is O(1) since we are moving only the pointers

    Soln 2 Recursively
    """

    def reverseList_soln1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, current_node = None, head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node

    def reverseList_soln2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList_soln2(head.next)
            head.next.next = head
        head.next = None

        return newHead
