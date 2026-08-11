class Solution(object):
    def backspaceCompare(self, s, t):
        def build (string):
            stack = deque()
            for char in string:

                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
                    
            return "".join(stack)
        
        return build(s)== build(t)
        
        
