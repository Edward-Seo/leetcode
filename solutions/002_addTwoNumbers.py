# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []
        l1_exit = 0
        l2_exit = 0
        l1_int = ''
        l2_int = ''
        
        while l1_exit == 0:
            l1_list.append(l1.val)
            if l1.next != None:
                l1 = l1.next
            else:
                l1_exit = 1
                
        while l2_exit == 0:
            l2_list.append(l2.val)
            if l2.next != None:
                l2 = l2.next
            else:
                l2_exit = 1
                
        l1_list.reverse()
        for i in l1_list:
            l1_int = l1_int + str(i)
        l1_int = int(l1_int)
        
        l2_list.reverse()
        for ii in l2_list:
            l2_int = l2_int + str(ii)
        l2_int = int(l2_int)
        
        number_added = l1_int + l2_int
        
        number_added = str(number_added)
        
        number_list = []
        for iii in number_added:
            number_list.append(int(iii))
        
        number_list.reverse()
        
        result = ListNode(number_list[0])
        first = result
        
        for i, ii in enumerate(number_list):
            if i > 0:
                result.next = ListNode(ii)
                result = result.next
                
        return first
