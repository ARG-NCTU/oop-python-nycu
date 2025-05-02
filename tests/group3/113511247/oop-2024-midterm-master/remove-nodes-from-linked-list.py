from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove every node which has a node with a greater value anywhere to the right side of it.

        Return the head of the modified linked list.

        Parameters:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The head of the modified linked list.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> head1 = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
            >>> result1 = solution.removeNodes(head1)
            >>> result1.val
            13
            >>> result1.next.val
            8
            >>> result1.next.next is None
            True

            # Example 2:
            >>> head2 = ListNode(1, ListNode(1, ListNode(1, ListNode(1))))
            >>> result2 = solution.removeNodes(head2)
            >>> result2.val
            1
            >>> result2.next.val
            1
            >>> result2.next.next.val
            1
            >>> result2.next.next.next.val
            1
            >>> result2.next.next.next.next is None
            True
        """
        def execute(head=head):
            if head is None:
                return 

            head.next = execute(head.next)
            return head.next if (head.next and head.val < head.next.val) else head

        return execute()
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)