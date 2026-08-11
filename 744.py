class Solution(object):
    def nextGreatestLetter(self, letters, target):
        low = 0
        high = len(letters) - 1
        while low <= high :
            mid = low + (high-low)/2 

            if letters[mid] <= target:
                low = mid+1
            else:
                high = mid-1
                
        return letters[low % len(letters)]
        
