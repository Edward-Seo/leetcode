# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if type(head) != ListNode:
            return None
        
        count = 0
        head_list = []
        while count == 0:
            head_list.append(head.val)
            if head.next:
                head = head.next
            else:
                count = 1
        
        new_head_list = []
        for i in head_list:
            if i not in new_head_list:
                new_head_list.append(i)
            else:
                pass
            
        result_1 = ListNode(new_head_list[0])
        result_0 = result_1
        
        for i, ii in enumerate(new_head_list):
            if i > 0:
                result_1.next = ListNode(ii)
                result_1 = result_1.next
        
        return result_0
