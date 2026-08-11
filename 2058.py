# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if head is None or head.next is None or head.next.next is None:
            return [-1,-1]
        
        critical_indices=[]
        prev=head
        curr=head.next
        index=1

        while curr.next is not None:
            is_peak = curr.val > prev.val and curr.val > curr.next.val
            is_valley = curr.val < prev.val and curr.val < curr.next.val

            if is_peak or is_valley:
                critical_indices.append(index)
            
            prev=curr
            curr=curr.next
            index=index+1

        if len(critical_indices) < 2:
            return [-1, -1]    
        
        max_dist = critical_indices[-1] - critical_indices[0]
        min_dist = float('inf')
        for i in range(1,len(critical_indices)):
            min_dist=min(min_dist,critical_indices[i]-critical_indices[i-1])
        
        return [min_dist,max_dist]
