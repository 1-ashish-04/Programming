# Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class Solution:
    def middleNode(self, head):
        l = head
        length = 0
        while(l):
            length += 1
            l = l.next
        
        length = (length)//2 + 1
        
        count = 0
        while(head):
            count += 1
            if count == length:
                l = head
            head = head.next
        
        while(l):
            print(l.val, end=" ")
            l = l.next

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

s = Solution()
s.middleNode(head)