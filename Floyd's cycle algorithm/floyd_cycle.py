class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def check_circle(ll):
    fast = ll
    slow = ll

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False

def start_point(ll):
    fast = ll
    slow = ll

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            slow = ll

            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow.value

    return None

ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)
ll.next.next.next.next.next = ListNode(6)
ll.next.next.next.next.next.next = ll.next.next

print(check_circle(ll))
print(start_point(ll))