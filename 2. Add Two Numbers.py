# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        num1_count,num2_count=0,0
        while l1:
            num1+=l1.val*(10**num1_count)
            num1_count+=1
            l1=l1.next
        while l2:
            num2+=l2.val*(10**num2_count)
            num2_count+=1
            l2=l2.next
        result=num1+num2
        if result==0:
            return ListNode(0)
        tmp=None
        result_listNode=None
        while True:
            val=result%10
            if result>0:
                if tmp is not None:
                    tmp.next=ListNode(val)
                    tmp=tmp.next
                else:
                    tmp = ListNode(val)
                    result_listNode=tmp
            else:
                break
            result=result//10

        return result_listNode

solution=Solution()
l1=tmp=ListNode(0)
tmp.next=ListNode(0)
tmp=tmp.next
tmp.next=ListNode(0)
tmp=tmp.next

l2=tmp=ListNode(0)
tmp.next=ListNode(0)
tmp=tmp.next
tmp.next=ListNode(0)
tmp=tmp.next

result=solution.addTwoNumbers(l1,l2)

while result:
    print(result.val)
    result=result.next