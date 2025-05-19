from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def execute(head: Optional[ListNode]) -> Optional[ListNode]:
            # 基底情況：如果節點為空，返回 None
            if head is None:
                return None
            
            # 遞迴處理後續節點
            head.next = execute(head.next)
            
            # 如果後續有更大值，移除當前節點；否則保留
            return head.next if (head.next and head.val < head.next.val) else head
        
        return execute(head)