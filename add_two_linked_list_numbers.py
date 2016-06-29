'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
class Solution1:
    '''
    using current as the cursor instead of the next node
    '''
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        node1 = l1
        node2 = l2
        root = ListNode(0) #value=0 is just a place holder so that root is NOT NONE
        current = root
        while node1 is not None or node2 is not None:
            if node1 is None:
                cur_value = current.val + node2.val
                node2 = node2.next
            elif node2 is None:
                cur_value = current.val + node1.val
                node1 = node1.next
            else:
                cur_value = current.val + node1.val + node2.val
                node1 = node1.next
                node2 = node2.next
            
            next_value = 0
            if cur_value >= 10:
                next_value = cur_value/10
                cur_value = cur_value%10    
                
            current.val = cur_value
            if node1 is None and node2 is None and next_value==0:
                break
            else:
                #reset cursor
                current.next = ListNode(next_value)
                current = current.next
            
        return root


class Solution2:
    '''    
    setting current firstly outside of the while loop
    '''
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        node1 = l1.next
        node2 = l2.next
        root = ListNode(l1.val + l2.val)
        current = root
        while node1 is not None or node2 is not None:
            current_value_1 = current.val%10
            current_value_2 = current.val/10
            
            current.val = current_value_1
            if node1 is None:
                next_value = current_value_2 + node2.val
                node2 = node2.next
            elif node2 is None:
                next_value = current_value_2 + node1.val
                node1 = node1.next
            else:
                next_value = current_value_2 + node1.val + node2.val
                node1 = node1.next
                node2 = node2.next
            current.next = ListNode(next_value)
            
            #reset cursor
            current = current.next
            
        #handle the last node     
        if current.val >= 10:
            current.next = ListNode(current.val/10)
            current.val = current.val%10

        return root