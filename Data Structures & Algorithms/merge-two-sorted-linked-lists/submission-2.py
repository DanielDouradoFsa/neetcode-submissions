# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        head = newList
        temp1 = list1
        temp2 = list2

        while temp1!=None and temp2!= None:
            if temp1.val >= temp2.val:
                newList.next = temp2
                temp2 = temp2.next
            else:
                newList.next = temp1
                temp1 = temp1.next
            newList = newList.next
        if temp1 == None:
            newList.next = temp2
        else:
            newList.next = temp1
        return head.next