class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums)
        for i in range(0,len(nums)):
            for j in range (1,len(nums)):
                index = (i+j) % len(nums)
                if nums[index] > nums[i]:
                    res[i]=nums[index]
                    break
           
        return res