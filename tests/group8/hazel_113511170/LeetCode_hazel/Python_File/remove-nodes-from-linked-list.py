class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNodes(self, head):
        if head==None:
            return None
        head.next=self.removeNodes(head.next)
        if head.next and head.val<head.next.val:
            return head.next
        else:
            return head     

        

n4=ListNode(0)
n3=ListNode(3,n4)
n2=ListNode(2,n3)
n1=ListNode(1,n2)
a=Solution()
ptr=a.removeNodes(n1)
for i in range(2):
    print(ptr.val)
    ptr=ptr.next    