class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=0
        for i in range(0,len(nums)):
            lar= nums[i]
            small= nums[i]
            for j in range(i+1,len(nums)):
                lar=max(lar,nums[j])
                small= min(small,nums[j])
                sum1+=lar-small
        return sum1