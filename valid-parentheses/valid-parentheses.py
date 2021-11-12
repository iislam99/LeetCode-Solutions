class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None or len(s)%2 != 0:
            return False
        
        left = {'(':1, '[':2, '{':3}
        right = {')':1, ']':2, '}':3}
        
        stack = []
        
        for char in s:
            if char in left:
                stack.append(char)
            elif stack and char in right:
                top = stack.pop()
                if left[top] != right[char]:
                    return False
            else:
                return False
        return (len(stack) == 0)