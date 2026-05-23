# Odd Even Linked List

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

class LinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def oddEvenList(self, head):
        l = head
        a = []
        while(l):
            a.append(l.val)
            l = l.next
        l = head
        for i in range(0, len(a), 2):
            l.val = a[i]
            l = l.next
        for i in range(1, len(a),2):
            l.val = a[i]
            l = l.next
        while(head):
            print(head.val, end=" ")
            head = head.next

head = LinkedList(1)
second = LinkedList(2)
third = LinkedList(3)
fourth = LinkedList(4)
fifth = LinkedList(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

s = Solution()
s.oddEvenList(head)