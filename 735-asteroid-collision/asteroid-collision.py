class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for i in asteroids:

            if stack == []:
                stack.append(i)
                continue

            if i > 0 and stack[-1] < 0 or i < 0 and stack[-1] > 0:

                while stack and i < 0 and stack[-1] > 0:

                    if abs(i) < abs(stack[-1]):
                        i = 0
                        break

                    elif abs(i) == abs(stack[-1]):
                        stack.pop()
                        i = 0
                        break

                    else:
                        stack.pop()

                if i != 0:
                    stack.append(i)

            else:
                stack.append(i)

        return stack
