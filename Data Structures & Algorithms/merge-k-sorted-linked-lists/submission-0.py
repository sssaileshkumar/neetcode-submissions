class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeList(l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next

                tail = tail.next

            if l1:
                tail.next = l1

            if l2:
                tail.next = l2

            return dummy.next

        def divide(left, right):
            if left == right:
                return lists[left]

            mid = (left + right) // 2

            l1 = divide(left, mid)
            l2 = divide(mid + 1, right)

            return mergeList(l1, l2)

        return divide(0, len(lists) - 1)