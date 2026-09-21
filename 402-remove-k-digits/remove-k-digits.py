class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        if k == len(num):
            return "0"

        for i in num:

            while stack and k > 0 and i < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(i)

        while k > 0:
            stack.pop()
            k -= 1
        ans = ''.join(stack).lstrip('0')

        if ans == "":
            return "0"

        return ans