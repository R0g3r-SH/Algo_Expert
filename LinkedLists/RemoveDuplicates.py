# Definition for singly-linked list.
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
    innode = head
    curr = innode.next
    while curr is not None:
        nextnode = curr.next
        while nextnode is not None and curr.val == nextnode.val:
            nextnode = nextnode.next
        innode.next = nextnode
        curr.next = nextnode
        curr=curr.next
        innode.next
    print("finalizo")
    return head

deleteDuplicates(head)