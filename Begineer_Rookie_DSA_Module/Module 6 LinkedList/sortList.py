# Sort List

# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

class ListNode:
    def __init__(self, val=0, next=None): # Create the Linked List
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        l = head # Create head point copy
        a = [] # List to store the value of the linkedlist

        while(l):
            a.append(l.val) # add Value into the list
            l = l.next

        a.sort()  # sort the list
        l = head
        i = 0

        while(l):
            l.val = a[i] # change the value in linked list, help of the list
            i += 1
            l = l.next

        while (head): # Print the sorted linked list
            print(head.val, end=" --> ")
            head = head.next
        print("None")

head = ListNode(4) # Linked list creation
second = ListNode(2) 
third = ListNode(1)
fourth = ListNode(3)
 
head.next = second # Connect the linked list
second.next = third
third.next = fourth

sol = Solution()
sol.sortList(head) # Print the sorted linked list