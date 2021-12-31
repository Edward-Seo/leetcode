You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_list = []
        second_list = []
        
        while list1:
            first_list.append(list1.val)
            list1 = list1.next
            
        while list2:
            second_list.append(list2.val)
            list2 = list2.next
        
        result_list = first_list + second_list
        
        result_list.sort()
        
        if len(result_list) == 0:
            return None
        
        answer = ListNode(result_list[0])
        result = answer
        
        for i, ii in enumerate(result_list):
            if i > 0:
                answer.next = ListNode(ii)
                answer = answer.next
                
        return result
