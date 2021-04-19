# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
# Given n will always be valid.
#
# Follow up:
# Could you do this in one pass?
from LinkedListx import linked_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=' ')
        curr = curr.next


def length_list(head):
    l = 0
    curr = head
    while curr:
        l += 1
        curr = curr.next
    return l


def remove_nth_from_end(head, n):
    l = length_list(head)
    i = 1
    curr = head
    for i in range(1, l):
        if i == l - n:
            curr.next = curr.next.next
            return head
        curr = curr.next
    if i == l - 1:
        head = head.next
        return head


# def remove_nth_from_end_one_pass(head, n):
#     l = 0
#     nodes = []
#     curr = head
#     while curr:
#         nodes.append(curr)
#         l += 1
#         curr = curr.next
#
#     if l == 1:
#         return None
#     i = l - n - 1
#     if i < 0:
#         head = head.next
#     else:
#         nodes[i].next = nodes[i].next.next
#     return head

def remove_nth_from_end_one_pass(head, n):
    curr = head
    prevn = head
    ctr = 0

    while curr:
        ctr += 1
        if ctr > n + 1:
            prevn = prevn.next
        curr = curr.next

    if prevn == head and ctr == n:
        head = head.next
    else:
        prevn.next = prevn.next.next

    return head


# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         slow = fast = head
#
#         for i in range(n):
#             fast = fast.next
#         if fast is None:
#             return head.next
#         while fast and fast.next:
#             fast = fast.next
#             slow = slow.next
#         slow.next = slow.next.next
#         return head

list1 = linked_list([1, 2, 3, 4, 5])
print(list1)
print(remove_nth_from_end(list1, 2))
