# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        q = deque()

        while head.next:
            q.append(head)
            head = head.next

        new_head = head

        while q:
            head.next = q.pop()
            head = head.next

        head.next = None

        return new_head
