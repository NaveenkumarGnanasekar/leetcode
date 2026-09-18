class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        left = [-1] * n
        right = [n] * n

        # Previous smaller
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)

        # Next smaller or equal
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]

            stack.append(i)

        total = 0

        for i in range(n):
            left_count = i - left[i]
            right_count = right[i] - i

            total += arr[i] * left_count * right_count
            total %= MOD

        return total