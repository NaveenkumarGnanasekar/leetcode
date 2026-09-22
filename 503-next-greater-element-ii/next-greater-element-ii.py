class Solution(object):
    def nextGreaterElements(self, nums):

        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):

            j = i % n

            while stack and stack[-1] <= nums[j]:
                stack.pop()

            if i < n and stack:
                ans[j] = stack[-1]

            stack.append(nums[j])

        return ans