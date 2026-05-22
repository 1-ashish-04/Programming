# Intersection of Two Linked list

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
# Note that the linked lists must retain their original structure after the function returns.

# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(Self, headA, headB):
        l = set()
        while(headA):
            l.add(headA)
            headA = headA.next
        while(headB):
            if headB in l:
                return headB
            headB = headB.next
        return None
    
    def printLinkedList(self, head):
        while(head):
            print(head.val, end = " ")
            head = head.next
    
headA= ListNode(4)
secondA = ListNode(1)
thirdA = ListNode(8)
fourthA = ListNode(4)
fifthA = ListNode(5)

headA.next = secondA
secondA.next = thirdA
thirdA.next = fourthA
fourthA.next = fifthA

headB = ListNode(5)
secondB = ListNode(6)
thirdB = ListNode(1)

headB.next = secondB
secondB.next = thirdB
thirdB.next = thirdA

s = Solution()
result = s.getIntersectionNode(headA, headB)
s.printLinkedList(result)