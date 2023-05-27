# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Second Time with Nodes, not really too familiar with it yet but i am getting the grasp of it
        slow = fast = head
        while fast and fast.next: # To know whether the next or the current faster pointer is in null. If it is in null it means that there is no cycle
            slow = slow.next
            fast = fast.next.next # Used the Tortoise and Hare Algo to find whether they meet and thus have a cycle
            if slow == fast:
                return True
        return False