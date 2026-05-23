# Remve Linked List Elements

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:

# Input: head = [], val = 1
# Output: []

# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    # def removeElements(self, head, val):
    #     a = [] # store values apart from an given val
    #     while(head):
    #         if head.val != val:
    #             a.append(head.val)
    #         head = head.next
    #     root = None
    #     for i in a:
    #         temp = ListNode(i) # new linked list created
    #         if root == None:
    #             root = temp
    #             head = temp
    #         else:
    #             root.next = temp # if already node is presented then then move to next node
    #             root = root.next
    #     while head: # Print the new list
    #         print(head.val, end=" ")
    #         head = head.next

    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        l = dummy
        while l.next:
            if l.next.val == val:
                l.next = l.next.next
            else:
                l = l.next
        l = dummy.next
        while l:
            print(l.val, end = " ")
            l = l.next

l = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(6)
fifth = ListNode(5)
sixth = ListNode(6)
l.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

s = Solution()
s.removeElements(l, 6)