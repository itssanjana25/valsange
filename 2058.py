# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if head is None or head.next is None or head.next.next is None:
            return [-1,-1]
        
        first_crit = -1
        last_crit = -1
        min_dist = float('inf')
        
        index = 1
        prev = head
        curr = head.next

        while curr.next is not None:
            nxt = curr.next

            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_crit == -1:
                    first_crit = index
                else:
                    min_dist = min(min_dist, index - last_crit)
                
                last_crit = index

            prev = curr
            curr = nxt
            index += 1
            
        if min_dist == float('inf'):
            return [-1, -1]
            
        max_dist = last_crit - first_crit
        
        return [min_dist, max_dist]

            

            
            
           
