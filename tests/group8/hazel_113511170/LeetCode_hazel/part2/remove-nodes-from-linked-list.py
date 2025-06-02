class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNodes(self,head):
        prev_nodes=[]
        curr=head
    
        while curr:
            while prev_nodes and prev_nodes[-1].val<curr.val:
                prev_nodes.pop()
            prev_nodes.append(curr)
            curr=curr.next

        for i in range(len(prev_nodes)-1):
            prev_nodes[i].next=prev_nodes[i+1]

        return prev_nodes[0]    

        

n4=ListNode(0)
n3=ListNode(3,n4)
n2=ListNode(2,n3)
n1=ListNode(1,n2)
a=Solution()
ptr=a.removeNodes(n1)
for i in range(2):
    print(ptr.val)
    ptr=ptr.next    