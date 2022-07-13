# Definition for singly-linked list.
from multiprocessing import dummy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l7 = ListNode(5)
l6 = ListNode(4, l7)
l5 = ListNode(4, l6)
l4 = ListNode(3, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
head = ListNode(1, l2)


def deleteDuplicates(head):
    #Base Case 
    if (head == None  or head.next is None):return head
    dumy = ListNode()
    dummy.next = head

    pre= dumy
    cur = head

    while cur is not None:
        
        if (cur.next != None and cur.val == cur.next.val):
            while (cur.next is not None and cur.val == cur.next.val):
                cur = cur.next
            pre.next = cur.next
        else:
            pre = cur
        
        cur= cur.next

    print("yeahhh")
    return dumy.next


deleteDuplicates(head)