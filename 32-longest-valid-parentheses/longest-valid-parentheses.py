class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        count = 0 
        if s == "":
            return 0
        for i,c in enumerate(s):
            if c =="(":
                stack.append(i)
            else :
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    count= max(count,i-stack[-1])
        return count