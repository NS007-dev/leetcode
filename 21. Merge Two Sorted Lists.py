# 21. Merge Two Sorted Lists
# Easy
# Topics
# premium lock iconCompanies

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create dummy node to anchor result list
        dummy = ListNode(-1)
        current = dummy

        # Compare elements from both lists attach smaller node
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach whichever list still remaining nodes
        current.next = list1 if list1 else list2

        # Return actual head (skipmthe dummy node)
        return dummy.next