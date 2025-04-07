class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev=None
        curr=head
        while curr:
            if prev:
                print("(curr {},prev {})".format(curr.val,prev.val))
            new_curr=curr.next
            curr.next=prev
            prev=curr
            curr=new_curr
            
        return prev
       

n3=ListNode(3)
n2=ListNode(2,n3)
n1=ListNode(1,n2)
a=Solution()
ptr=a.reverseList(n1)
for i in range(3):
    print(ptr.val)
    ptr=ptr.next



        