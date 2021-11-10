# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        count = 0
        while l1:
            num1 += (l1.val * 10**count)
            count += 1
            l1 = l1.next
        
        num2 = 0
        count = 0
        while l2:
            num2 += (l2.val * 10**count)
            count += 1
            l2 = l2.next
        
        num1 += num2
        
        digit = num1 % 10
        head = ListNode(digit, None)
        temp = head
        num1 /= 10
        
        while num1:
            digit = num1 % 10
            num1 /= 10
            temp.next = ListNode(digit, None)
            temp = temp.next
        
        return head