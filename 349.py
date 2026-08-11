class Solution(object):
    def intersection(self, num1, num2):
        return list(set(num1) & set(num2))
        num1 = [1,2,2,1]
        num2 = [2,2]
       

        print(intersection(num1,num2))
        print(intersection([4,9,5],[9,4,9,8,4]))
       
        
