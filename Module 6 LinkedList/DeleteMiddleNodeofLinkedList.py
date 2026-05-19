# Delete the Middle Node of a Linked List

# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

#     For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

# Example 1:

# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 

# Example 2:

# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.

# if head [] or [1] --> then return []

class  ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteMiddleNode(self, head):
        if head == None or head.next == None:
            print ("None")
            return 
        l = head
        length = 0
        while(l):
            length += 1
            l = l.next
        l = head
        length //= 2

        count = 0
        while(l):
            
            if count == length-1:  # For 0 based  indexing 
                l.next = l.next.next
                break
            l = l.next
            count += 1
        while(head):
            print(head.val, end = " ")
            head = head.next
    
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
s.deleteMiddleNode(head)