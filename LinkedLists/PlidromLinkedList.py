
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n4 = ListNode(1)
n3 = ListNode(2)
n2 = ListNode(2)
n1 = ListNode(2)
head = ListNode(1)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


def isPalindrome(head):
    curr = head
    fast = head
    stak = 0
    if curr.next is None:
        return True
    while(fast is not None and curr.next is not None):
        stak += curr.val
        fast = fast.next.next
        curr = curr.next
        if fast is not None:

            if fast.next is None:
                stak += curr.val
                break
    while(curr is not None):
        val = curr.val if curr else 0
        stak -= val
        curr = curr.next
    return stak == 0


isPalindrome(head)
