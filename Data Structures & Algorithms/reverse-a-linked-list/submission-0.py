# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_temp = None
        current_val = head

        while current_val:
            next_val = current_val.next
            current_val.next = previous_temp
            previous_temp = current_val
            current_val = next_val
        return previous_temp
