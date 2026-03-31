# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Have to remove n from the tail
        #n_head = len_list - n

        #approach:
        #Discover the len of the list:
            #Discover the len: O(n)
            #Iterate list and if actual index = #n_head = len_list - n: O(N-n)
                #drop this position
        len_list = 0
        head_temp = head
        while head_temp:
            head_temp = head_temp.next
            len_list+=1
        n_head = len_list - n
        if not n_head:
            return head.next
        head_temp = head
        while head_temp:
            n_head -= 1
            if n_head == 0:
                new_next = head_temp.next.next if head_temp.next else None
                head_temp.next = new_next
            head_temp = head_temp.next
        return head