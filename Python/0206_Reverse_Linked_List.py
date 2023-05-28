# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , curr = None, head # initialising
        while curr:
            nxt = curr.next # keep curr.next
            curr.next = prev # since prev is None, curr.nexxt will be None thus curr will be the last Node
            prev = curr # prev then will be the Last Node
            curr = nxt # curr will continue at the start as the second Node to keep the while loop running
        return prev