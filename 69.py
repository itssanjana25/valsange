class Solution(object):
    def mySqrt(self, x):
        if x<=3 & x>0:
            return 1
        elif x == 0:
            return 0
        
        low = 0
        high = x/2
        ans = 0
        while low <= high :
            mid = low + (high-low)/2
            square = mid*mid
            if square == x:
                return mid
            elif square<x:
                ans = mid
                low = mid+1
            else:
                high = mid -1

        return ans


        
