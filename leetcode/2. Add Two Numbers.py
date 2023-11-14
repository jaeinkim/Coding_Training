# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
#
# =========== START: Description ===========
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
# Constraints:
#
# - The number of nodes in each linked list is in the range [1, 100].
# - 0 <= Node.val <= 9
# - It is guaranteed that the list represents a number that does not have leading zeros.
# =========== END: Description ===========


    # 첫번째 시도. Time Limit Exceeded 발생(23/11/14 화 기준)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        # print(l1.val)
        # print(l1.next)
        # # print(l1.next.val)
        # print(l1.val)
        # print('a' if None else 'b')
        a = 0
        answer = ListNode()
        n1, n2 = l1.val, l2.val
        while True:

            answer.next = ListNode(val = ((n1+n2)%10)+a)
            a = (n1+n2)//10
            n1 = 0 if l1.next is None else l1.next.val
            n2 = 0 if l2.next is None else l2.next.val
            if l1 is None and l2 is None:
                break
        return answer.next



# 두 번째 시도. 풀이보고 함
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val //10
            val = val % 10
            cur.next = ListNode(val=val)

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
