class Solution(object):
    def countSmaller(self, nums):
        sorted_nums = sorted(set(nums))

        rank = {}
        for i in range(len(sorted_nums)):
            rank[sorted_nums[i]] = i + 1
        n = len(sorted_nums)
        bit = [0] * (n + 1)

        def update(index):
            while index <= n:
                bit[index] += 1
                index += index & -index

        def query(index):
            total = 0

            while index > 0:
                total += bit[index]
                index -= index & -index

            return total

        ans = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):

            r = rank[nums[i]]

            ans[i] = query(r - 1)
            update(r)

        return ans