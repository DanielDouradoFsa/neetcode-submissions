# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        #Input: head = [0,1,2,3]
        #Output: [3,2,1,0]
        #Prev = None
        #curr = 0
        #next_temp = curr.next, salva o 1
        #curr.next = prev, 0 aponta para o None
        #prev = curr, antes None, agora 0
        #curr = temp, referencia que era 0 agora é 1
        #
        prev, curr = None,head
        while curr:
            next_temp = curr.next #1
            curr.next = prev #0->None
            prev = curr
            curr = next_temp
        return prev




        