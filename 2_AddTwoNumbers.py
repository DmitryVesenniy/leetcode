# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# import math

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return None
        
        l1_list = []
        l2_list = []
        while True:
            if l1:
                l1_list.append(l1.val)
                l1 = l1.next
                
            if l2:
                l2_list.append(l2.val)
                l2 = l2.next
                
            if not l1 and not l2:
                break
        
        val_from_l1 = self.convert_to_int(l1_list[::-1])
        val_from_l2 = self.convert_to_int(l2_list[::-1])
        
        result = val_from_l1 + val_from_l2
        list_result = self.convert_to_list_fake(result)[::-1]
        
        l_result = ListNode(list_result[0])
        current_node = l_result
        for i in list_result[1:]:
            node = ListNode(i)
            current_node.next = node
            current_node = node
            
        return l_result
            
    def convert_to_int(self, l: list[int]) -> int:
        val = 0
        degree = len(l) - 1

        for _val in l:
            val += _val * 10 ** degree
            degree -= 1

        return val
    
    def convert_to_list_fake(self, val: int) -> list[int]:
        return list(map(lambda x: int(x), list(str(val))))

    def convert_to_list(self, val: int) -> list[int]:
        import math
        
        degree = int(math.log10(val))
        result = []
        for i in range(degree, 0, -1):
            v = val // 10 ** i
            result.append(v%10)
        result.append(val%10)
        return result