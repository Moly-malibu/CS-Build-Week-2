# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Marta's solution
#
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        
        cur = head
        while cur is not None:   # O(n)
            values.append(cur.val)
            cur = cur.next
            
        values_reversed = list(reversed(values)) # O(n)
        
        return values == values_reversed  # O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Barbara's solution, Beej's complex implementation
#
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        length = 0
        
        while cur is not None:
            length += 1
            cur = cur.next
            
        stack = []
        
        cur = head
        index = 0
        halfway_index = length // 2
        
        while cur is not None:
            if not(length % 2 == 1 and index == halfway_index):

                if index < halfway_index:
                    stack.append(cur.val)

                elif index >= halfway_index:
                    if stack == []:
                        return False

                    val = stack.pop()
                    if val != cur.val:
                        return False
                
            cur = cur.next
            index += 1
        
        if stack != []:
            return False
        
        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Barbara's solution, Matthew's simplification
#
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        stack = []
        
        while cur is not None:
            stack.append(cur.val)
            cur = cur.next
            
        cur = head
        while cur is not None:
            val = stack.pop()
            if val != cur.val:
                return False
                
            cur = cur.next
        
        return True
