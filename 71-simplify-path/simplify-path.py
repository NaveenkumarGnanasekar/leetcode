class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        a = path.split("/")
        stack =[]
        for b in a :
            if b =="" or b==".":
                continue
            elif b == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(b)
        return "/" +"/".join(stack)