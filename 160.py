# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None

        p1 = headA
        p2 = headB
        while p1 is not p2:
            if p1 == None:
                 p1 = headB
           
            else:
                p1 = p1.next

            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next

        return p1
        

    

        
