from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    @classmethod
    def from_list(cls, values):
        head = ListNode()
        current = head
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return head.next

    def to_list(self):
        values = []
        current = self
        while current:
            values.append(current.val)
            current = current.next
        return values
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list and return the reversed list.

        Parameters:
            head (Optional[ListNode]): The head of the original linked list.

        Returns:
            Optional[ListNode]: The head of the reversed linked list.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> head1 = ListNode.from_list([1, 2, 3, 4, 5])
            >>> reversed_head1 = solution.reverseList(head1)
            >>> reversed_head1.to_list()
            [5, 4, 3, 2, 1]

            # Example 2:
            >>> head2 = ListNode.from_list([1, 2])
            >>> reversed_head2 = solution.reverseList(head2)
            >>> reversed_head2.to_list()
            [2, 1]

            # Example 3:
            >>> head3 = None
            >>> reversed_head3 = solution.reverseList(head3)
            >>> reversed_head3 is None
            True
        """
        
        new_head = head

        if head and head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None

        return new_head
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    