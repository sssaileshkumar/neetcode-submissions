# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        curr = head

        while curr:
            counter += 1
            curr = curr.next
        
        middle = counter//2

        curr = head
        counter = 0

        while counter != middle:
            curr = curr.next
            counter += 1
        return curr