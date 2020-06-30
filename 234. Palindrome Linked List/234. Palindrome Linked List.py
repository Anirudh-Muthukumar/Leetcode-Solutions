# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, head):
        if not head:
            return head
        prev = None
        curr = head
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def isPalindrome(self, head):        
        # palindrome is symmetric
        slow, fast = head, head
        ct = 0 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = self.reverse(slow)
        
        while mid:
            if mid.val!=head.val:
                return False
            mid = mid.next
            head = head.next
        
        return True
        