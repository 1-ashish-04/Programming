# Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def hasCycle(self, head):
        s = set()
        while(head != None):
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
    
# Creating linked list: 3 -> 2 -> 0 -> -4
head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

head.next = second
second.next = third
third.next = fourth

# Creating cycle: tail connects to node at index 1 (value = 2)
fourth.next = second


sol = Solution()
print(sol.hasCycle(head)) 